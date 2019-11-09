//---------------------------------
// 2016/8/24

#ifndef LCDAQM_H
#define LCDAQM_H


//---------------------------------
// Constant



//---------------------------------
// Class

class LCDAQM{
private:
	//---------------------------------
	// Constant
	static const uint8_t i2cAdr = 0x3E;


	//---------------------------------
	// Variable

	int i2c;			// I2C

	uint8_t count;		// Character count in line
	uint8_t line;	// 1:1st line, 2:2nd line


	//---------------------------------
	// Function
	void writeData(uint8_t ctrl, uint8_t data);


public:
	//---------------------------------
	// Function
	LCDAQM();
	uint8_t init();
	void closeI2C();
	void printStr(char*str);
	void clear();
	void home();
	void secLine();
};

#endif

