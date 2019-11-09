//---------------------------------
// 2016/9/3

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <stdbool.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/ioctl.h>
#include <linux/i2c-dev.h>
#include "BME280I2C.h"


//---------------------------------
// Private Class Function

// Read length Byte from address by I2C
void BME280I2C::readAddress(uint8_t addr, uint8_t*data, uint32_t length){
	uint8_t buf[1];
	buf[0]=addr;
	if(write(i2c,buf,1) == 1){
		read(i2c,data,length);
	}
	return;
}

// Write 1Byte at specific address by I2C
void BME280I2C::writeAddress(uint8_t addr, uint8_t data){
	uint8_t buf[2];
	buf[0]=addr;
	buf[1]=data;
	write(i2c,buf,2);
	return;
}

// ID Read by I2C
uint8_t BME280I2C::idRead(){
	uint8_t data[1];
	readAddress(0xD0, data, 1);
	if(data[0]!=0x60){
		return 1;
	}
	return 0;
}

// Status read
uint8_t BME280I2C::statusRead(){
	uint8_t data[1];
	readAddress(0xF3, data, 1);
	return data[0]&0x9;
}

// Read calibration
void BME280I2C::readCalibration(){
	uint8_t buf[2];
	readAddress(0x88, cal.byte, calLengthTP);	// Cal T and P are read sequentially

	// H1
	readAddress(0xA1, buf, 1);
	cal.byte[24] = buf[0];

	// H2
	readAddress(0xE1, buf, 1);
	cal.byte[26] = buf[0];
	readAddress(0xE2, buf, 1);
	cal.byte[27] = buf[0];

	// H3
	readAddress(0xE3, buf, 1);
	cal.byte[28] = buf[0];

	// H4
	readAddress(0xE4, buf, 2);
	cal.byte[30] = ((buf[0]&0xF)<<4)+(buf[1]&0xF);
	cal.byte[31] = buf[0]>>4;

	// H5
	readAddress(0xE5, buf, 2);
	cal.byte[32] = (buf[0]>>4)+((buf[1]&0xF)<<4);
	cal.byte[33] = buf[1]>>4;

	// H6
	readAddress(0xE7, buf, 1);
	cal.byte[34] = buf[0];
}


// Read ADC registers of T, P and H
// Calculated compensate data
void BME280I2C::readMeas(){
	uint8_t buf[8];
	readAddress(0xF7, buf, 8);
	adcP = (buf[0]<<12) + (buf[1]<<4) + (buf[2]>>4);
	adcT = (buf[3]<<12) + (buf[4]<<4) + (buf[5]>>4);
	adcH = (buf[6]<<8) + buf[7];
	cT = compensate_T_int32(adcT);
	cP = compensate_P_int64(adcP);
	cH = compensate_H_int32(adcH);
	T = ((float)(int32_t)cT/100);
	P = ((float)cP)/25600;
	H = ((float)cH)/1024;
}

// Measure forced mode, x1 over sampling, no filter
void BME280I2C::forced(){
	writeAddress(0xF5, 0x0);	// config
	writeAddress(0xF2, 0x5);	// ctrl_hum, oversampling x16
	writeAddress(0xF4, 0xB5);	// ctrl_meas, oversampling x16, forced mode
	while(0!=statusRead()){
		usleep(1);
	}
}


// Returns temperature in DegC, resolution is 0.01 DegC. Output value of "5123" equals 51.23 DegC.
// t_fine carries fine temperature as global value
BME280_S32_t BME280I2C::compensate_T_int32(BME280_S32_t adc_T)
{
	BME280_S32_t var1, var2, T;
	var1  = ((((adc_T>>3) - ((BME280_S32_t)cal.dig_T1<<1))) * ((BME280_S32_t)cal.dig_T2)) >> 11;
	var2  = (((((adc_T>>4) - ((BME280_S32_t)cal.dig_T1)) * ((adc_T>>4) - ((BME280_S32_t)cal.dig_T1))) >> 12) *
		((BME280_S32_t)cal.dig_T3)) >> 14;
	t_fine = var1 + var2;
	T  = (t_fine * 5 + 128) >> 8;
	return T;
}

// Returns pressure in Pa as unsigned 32 bit integer in Q24.8 format (24 integer bits and 8 fractional bits).
// Output value of "24674867" represents 24674867/256 = 96386.2 Pa = 963.862 hPa
BME280_U32_t BME280I2C::compensate_P_int64(BME280_S32_t adc_P)
{
	BME280_S64_t var1, var2, p;
	var1 = ((BME280_S64_t)t_fine) - 128000;
	var2 = var1 * var1 * (BME280_S64_t)cal.dig_P6;
	var2 = var2 + ((var1*(BME280_S64_t)cal.dig_P5)<<17);
	var2 = var2 + (((BME280_S64_t)cal.dig_P4)<<35);
	var1 = ((var1 * var1 * (BME280_S64_t)cal.dig_P3)>>8) + ((var1 * (BME280_S64_t)cal.dig_P2)<<12);
	var1 = (((((BME280_S64_t)1)<<47)+var1))*((BME280_S64_t)cal.dig_P1)>>33;
	if (var1 == 0)
	{
		return 0; // avoid exception caused by division by zero
	}
	p = 1048576-adc_P;
	p = (((p<<31)-var2)*3125)/var1;
	var1 = (((BME280_S64_t)cal.dig_P9) * (p>>13) * (p>>13)) >> 25;
	var2 = (((BME280_S64_t)cal.dig_P8) * p) >> 19;
	p = ((p + var1 + var2) >> 8) + (((BME280_S64_t)cal.dig_P7)<<4);
	return (BME280_U32_t)p;
}

// Returns humidity in %RH as unsigned 32 bit integer in Q22.10 format (22 integer and 10 fractional bits).
// Output value of "47445" represents 47445/1024 = 46.333 %RH
BME280_U32_t BME280I2C::compensate_H_int32(BME280_S32_t adc_H)
{
	BME280_S32_t v_x1_u32r;
	v_x1_u32r = (t_fine - ((BME280_S32_t)76800));
	v_x1_u32r = (((((adc_H << 14) - (((BME280_S32_t)cal.dig_H4) << 20) - (((BME280_S32_t)cal.dig_H5) * v_x1_u32r)) +
		((BME280_S32_t)16384)) >> 15) * (((((((v_x1_u32r * ((BME280_S32_t)cal.dig_H6)) >> 10) * (((v_x1_u32r *
		((BME280_S32_t)cal.dig_H3)) >> 11) + ((BME280_S32_t)32768))) >> 10) + ((BME280_S32_t)2097152)) *
		((BME280_S32_t)cal.dig_H2) + 8192) >> 14));
	v_x1_u32r = (v_x1_u32r - (((((v_x1_u32r >> 15) * (v_x1_u32r >> 15)) >> 7) * ((BME280_S32_t)cal.dig_H1)) >> 4));
	v_x1_u32r = (v_x1_u32r < 0 ? 0 : v_x1_u32r);
	v_x1_u32r = (v_x1_u32r > 419430400 ? 419430400 : v_x1_u32r);
	return (BME280_U32_t)(v_x1_u32r>>12); 
}


//---------------------------------
// Public Class Function

BME280I2C::BME280I2C(){
	stat = statNotStarted;
	adcT = 0;
	adcP = 0;
	adcH = 0;
	cT = 0;
	cP = 0;
	cH = 0;
	T = 0;
	P = 0;
	H = 0;

	for(uint8_t i=0; i<calLength; i++){
		cal.byte[i] = 0;
	}
}


// Initialize BME280
//  Return 0 if success
uint8_t BME280I2C::meas(int i2cAdr){
	// Not BME280 I2C address
	if(i2cAdr!=0x76 && i2cAdr!=0x77){
		stat = statI2CError;
		return stat;
	}

	// Open I2C
	i2c = open("/dev/i2c-1",O_RDWR);
	if(i2c<0){
		stat = statI2CError;
		return stat;
	}

	// Set I2C Address
	if(ioctl(i2c, I2C_SLAVE, i2cAdr)<0){
		close(i2c);
		stat = statI2CError;
		return stat;
	}

	// ID Read
	if(0!=idRead()){
		close(i2c);
		stat = statSensorError;
		return stat;
	}

	readCalibration();
	forced();
	readMeas();

	close(i2c);

	stat = statSuccess;
	return stat;
}


// Return true if measurement is done
bool BME280I2C::getResult(){
	if(stat == statSuccess){
		return true;
	}else{
		return false;
	}
}


// Print calibration
void BME280I2C::printCalibration(){
	printf("Calibration Data\n");
	printf(" dig_T1 : %d\n", cal.dig_T1);
	printf(" dig_T2 : %d\n", cal.dig_T2);
	printf(" dig_T3 : %d\n", cal.dig_T3);
	printf(" dig_P1 : %d\n", cal.dig_P1);
	printf(" dig_P2 : %d\n", cal.dig_P2);
	printf(" dig_P3 : %d\n", cal.dig_P3);
	printf(" dig_P4 : %d\n", cal.dig_P4);
	printf(" dig_P5 : %d\n", cal.dig_P5);
	printf(" dig_P6 : %d\n", cal.dig_P6);
	printf(" dig_P7 : %d\n", cal.dig_P7);
	printf(" dig_P8 : %d\n", cal.dig_P8);
	printf(" dig_P9 : %d\n", cal.dig_P9);
	printf(" dig_H1 : %d\n", cal.dig_H1);
	printf(" dig_H2 : %d\n", cal.dig_H2);
	printf(" dig_H3 : %d\n", cal.dig_H3);
	printf(" dig_H4 : %d\n", cal.dig_H4);
	printf(" dig_H5 : %d\n", cal.dig_H5);
	printf(" dig_H6 : %d\n", cal.dig_H6);
}

// Print ADC and compensated register
void BME280I2C::printRegister(){
	printf("Register Data\n");
	printf(" ADC T : %x\n", adcT);
	printf(" ADC P : %x\n", adcP);
	printf(" ADC H : %x\n", adcH);
	printf(" cT : %d\n", cT);
	printf(" cP : %d\n", cP);
	printf(" cH : %d\n", cH);
}

// Print Measurement data
void BME280I2C::printMeas(){
	printf("Measured Data\n");
	printf(" Temp : %.1fC\n", T);
	printf(" Pressure : %.2fhPa\n", P);
	printf(" Humidity : %.1f%%\n", H);
}

// Get T, P or H
float BME280I2C::getMeas(uint8_t select){
	switch(select){
	case selectTemp:
		return T;
	case selectPressure:
		return P;
	case selectHumidity:
		return H;
	default:
		return 0;
	}
}









