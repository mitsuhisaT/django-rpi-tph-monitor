//---------------------------------
// 2016/9/3

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
#include "InfraredLED.h"



//---------------------------------
// Private Class Function

// Send one pulse from LED
//  Parameter
//   length : length x26 [us]
void InfraredLED::pulse(uint16_t lengthON, uint16_t lengthOFF){
	// ON with 38kHz carrier
	for(uint16_t i=0; i<lengthON; i++){
		digitalWrite(ledGPIO, 1);
		delayMicroseconds(8);
		digitalWrite(ledGPIO, 0);
		delayMicroseconds(18);
	}
	
	// OFF
	for(uint16_t i=0; i<lengthOFF; i++){
		delayMicroseconds(26);
	}
}

void InfraredLED::sendLead(uint8_t format){
	switch(format){
	case formatAEHA:
		pulse(130,65);
		break;
	case formatNEC:
		pulse(346,173);
		break;
	default:
		return;
	}
}

void InfraredLED::sendByte(uint8_t format, uint8_t data){
	uint16_t t;
	
	switch(format){
	case formatAEHA:
		t=16;
		break;
	case formatNEC:
		t=22;
		break;
	default:
		return;
	}
	
	for(uint8_t b=0; b<=7; b++){
		if(((data>>b)&0x1) == 0){
			pulse(t,t);
		}else{
			pulse(t,t*3);
		}
	}
}

void InfraredLED::sendStop(uint8_t format){
	switch(format){
	case formatAEHA:
		pulse(16,0);
		break;
	case formatNEC:
		pulse(22,0);
		break;
	default:
		return;
	}
	delayMicroseconds(9000);
}



//---------------------------------
// Public Class Function

InfraredLED::InfraredLED(uint8_t setGPIO){
	ledGPIO = setGPIO;
	pinMode(ledGPIO, OUTPUT);
}

void InfraredLED::sendFrame(uint8_t format, uint8_t*data, uint32_t length){
	pinMode(ledGPIO, OUTPUT);

	sendLead(format);
	for(uint32_t i=0; i<length; i++){
		sendByte(format, data[i]);
	}
	sendStop(format);
}


