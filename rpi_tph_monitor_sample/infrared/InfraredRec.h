//---------------------------------
// 2016/10/29

#ifndef INFRAREDREC_H
#define INFRAREDREC_H



//---------------------------------
// Class

class InfraredRec{
private:
	//---------------------------------
	// Constant
	static const uint8_t maxFrameSize = 32;	// Receiver buffer max frame size
	static const uint8_t maxFrameCount = 8;	// Receiver buffer max frame count

	//---------------------------------
	// Variable
	uint8_t recGPIO;	// Receiver GPIO


	//---------------------------------
	// Function
	
	uint32_t receivePulse(bool timeout);
	uint8_t checkFormat(uint32_t firstPulse);
	bool checkRepeat(uint8_t format, uint32_t firstPulse);
	uint8_t readFrame(uint8_t*buf, bool timeout);


public:
	//---------------------------------
	// Constant

	// Infrared Format
	static const uint8_t formatUnknown = 0;
	static const uint8_t formatNEC = 1;
	static const uint8_t formatAEHA = 2;
	static const uint8_t formatSONY = 3;


	//---------------------------------
	// Variable
	uint8_t format;	// Last received foramt type
	uint8_t frameCount;	// Received frame count
	uint8_t frameSize[maxFrameSize];	// Received frame size
	uint8_t frameData[maxFrameCount][maxFrameSize];	// Received frame data


	//---------------------------------
	// Function
	InfraredRec(uint8_t setGPIO);
	void readData();
};

#endif

