//---------------------------------
// 2016/8/24

#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>
#include <string.h>
#include <stdbool.h>
#include <time.h>
#include <unistd.h>
#include <fcntl.h>
#include <wiringPi.h>
#include <sys/stat.h>
#include <sys/ioctl.h>
#include <linux/i2c-dev.h>
#include "LCDAQM.h"


//---------------------------------
// Private Class Function

// Write control and data by I2C
void LCDAQM::writeData(uint8_t ctrl, uint8_t data){
	uint8_t buf[2];
	buf[0]=ctrl;
	buf[1]=data;
	write(i2c,buf,2);
	delayMicroseconds(50);
	return;
}



//---------------------------------
// Public Class Function

LCDAQM::LCDAQM(){
	count = 0;
	line = 1;
}


// Initialize LCD
//  Return 0 if success
uint8_t LCDAQM::init(){
	// Open I2C
	i2c = open("/dev/i2c-1",O_RDWR);
	if(i2c<0){
		return 1;
	}

	// Set I2C Address
	if(ioctl(i2c, I2C_SLAVE, i2cAdr)<0){
		close(i2c);
		return 1;
	}
	delay(50);

	writeData(0, 0x38);
	writeData(0, 0x39);
	writeData(0, 0x14);
	writeData(0, 0x70);
	writeData(0, 0x56);
	writeData(0, 0x6C);
	delay(250);
	writeData(0, 0x38);
	writeData(0, 0x0C);
	clear();

	return 0;
}

void LCDAQM::closeI2C(){
	close(i2c);
}

void LCDAQM::printStr(char*str){
	for(uint8_t i=0; i<16; i++){
		// Null character
		if(str[i]==0){
			return;
		}
		count++;
		if(count>8){
			if(line==2){
				home();
			}else{
				secLine();
			}
		}
		writeData(0x40, str[i]);
	}
}

void LCDAQM::clear(){
	count = 0;
	line = 1;
	writeData(0, 0x01);
	delay(2);
}


void LCDAQM::home(){
	count = 0;
	line = 1;
	writeData(0, 0x02);
	delay(2);
}


void LCDAQM::secLine(){
	count = 0;
	line = 2;
	writeData(0, 0xC0);
}









