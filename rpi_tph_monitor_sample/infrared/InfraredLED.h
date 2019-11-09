//---------------------------------
// 2016/9/3

#ifndef INFRAREDLED_H
#define INFRAREDLED_H



//---------------------------------
// Class

class InfraredLED{
private:
	//---------------------------------
	// Variable
	uint8_t ledGPIO;	// LED GPIO


	//---------------------------------
	// Function
	
	void pulse(uint16_t lengthON, uint16_t lengthOFF);
	void sendLead(uint8_t format);
	void sendByte(uint8_t format, uint8_t data);
	void sendStop(uint8_t format);
	
public:
	//---------------------------------
	// Constant
	
	// Infrared Format
	static const uint8_t formatUnknown = 0;
	static const uint8_t formatNEC = 1;
	static const uint8_t formatAEHA = 2;
	static const uint8_t formatSONY = 3;


	//---------------------------------
	// Function
	InfraredLED(uint8_t setGPIO);
	void sendFrame(uint8_t format, uint8_t*data, uint32_t length);
};

#endif

