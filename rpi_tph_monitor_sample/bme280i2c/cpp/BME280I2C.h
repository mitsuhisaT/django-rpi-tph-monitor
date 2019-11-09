//---------------------------------
// 2016/9/3

#ifndef BME280I2C_H
#define BME280I2C_H


//---------------------------------
// Constant

#define BME280_S32_t	int32_t
#define BME280_S64_t	int64_t
#define BME280_U32_t	uint32_t


//---------------------------------
// Class

class BME280I2C{
private:
	//---------------------------------
	// Constant

	static const uint8_t calLength = 38;
	static const uint8_t calLengthTP = 24;


	//---------------------------------
	// Type

	union Calibration{
		uint8_t byte[calLength];
		struct{
			uint16_t dig_T1;
			int16_t dig_T2;
			int16_t dig_T3;
			uint16_t dig_P1;
			int16_t dig_P2;
			int16_t dig_P3;
			int16_t dig_P4;
			int16_t dig_P5;
			int16_t dig_P6;
			int16_t dig_P7;
			int16_t dig_P8;
			int16_t dig_P9;
			uint8_t dig_H1;
			uint8_t dummy;
			int16_t dig_H2;
			uint8_t dig_H3;
			uint8_t dummy2;
			int16_t dig_H4;
			int16_t dig_H5;
			int8_t dig_H6;
		};
	};


	//---------------------------------
	// Variable

	// Status
	uint8_t stat;

	// I2C
	int i2c;

	// Calibration data
	union Calibration cal;

	// Temperature for calculation
	BME280_S32_t t_fine;

	// ADC T, P, H
	uint32_t adcT;
	uint32_t adcP;
	uint32_t adcH;
	int32_t cT;
	uint32_t cP;
	uint32_t cH;
	float T;	// Degree C
	float P;	// hPa
	float H;	// %

	//---------------------------------
	// Function
	
	void readAddress(uint8_t addr, uint8_t*data, uint32_t length);
	void writeAddress(uint8_t addr, uint8_t data);
	uint8_t idRead();
	uint8_t statusRead();
	void readCalibration();
	void readMeas();
	void forced();
	BME280_S32_t compensate_T_int32(BME280_S32_t adc_T);
	BME280_U32_t compensate_P_int64(BME280_S32_t adc_P);
	BME280_U32_t compensate_H_int32(BME280_S32_t adc_H);


public:
	//---------------------------------
	// Constant

	// getMeas select
	static const uint8_t selectTemp = 1;
	static const uint8_t selectPressure = 2;
	static const uint8_t selectHumidity = 3;

	// meas status code
	static const uint8_t statSuccess = 0;
	static const uint8_t statNotStarted = 1;
	static const uint8_t statI2CError = 2;
	static const uint8_t statSensorError = 3;

	//---------------------------------
	// Function

	BME280I2C();
	uint8_t meas(int i2cAdr);
	bool getResult();
	void printCalibration();
	void printRegister();
	void printMeas();
	float getMeas(uint8_t select);
};

#endif

