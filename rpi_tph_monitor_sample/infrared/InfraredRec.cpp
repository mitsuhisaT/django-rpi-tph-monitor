//---------------------------------
// 2016/10/29

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
#include "InfraredRec.h"



//---------------------------------
// Private Class Function


// Receive one on/off pulse and return length
//  Parameter
//   timeout : return if timeout
//  Return
//   Low 16bit : ON pulse [us] / 10
//   High 16bit : OFF pulse [us] / 10
//   0xFFFF : Timeout
uint32_t InfraredRec::receivePulse(bool timeout){
	uint16_t to=0;
	uint16_t on=0;
	uint16_t off=0;

	// Wait ON pulse
	while(1==digitalRead(recGPIO)){
		to++;
		if(to>50000 && timeout){
			return 0x0000FFFF;
		}
		delayMicroseconds(1);
	}

	// ON pulse
	while(0==digitalRead(recGPIO)){
		delayMicroseconds(10);
		on++;
	}
	uint16_t l = on*8;	// Timeout limit
	
	// OFF pulse
	while(1==digitalRead(recGPIO)){
		delayMicroseconds(10);
		off++;
		if(off>l){
			break;
		}
	}

	uint32_t r = off;
	r = r <<16;
	r = r | on;
	return r;
}

uint8_t InfraredRec::checkFormat(uint32_t firstPulse){
	uint16_t on = firstPulse & 0xFFFF;
	uint16_t off = firstPulse >> 16;
	
	if(on>280 && on<400){
		return formatAEHA;
	}
	if(on>750 && on<1000){
		return formatNEC;
	}
	if(on>180 && on<280){
		return formatSONY;
	}
	return formatUnknown;
}

// Return true if repeat signal
bool InfraredRec::checkRepeat(uint8_t format, uint32_t firstPulse){
	uint16_t off = firstPulse >> 16;
	
	switch(format){
	case formatAEHA:
		if(off>270){
			return true;
		}
		return false;
	case formatNEC:
		if(off<338){
			return true;
		}
		return false;
	}
	return false;
}


// NEC and AEHA format only
//  Write to buffer, max 64bytes
//  Return
//   Number of read data
//   0xFF : Not support format or error
//   0xFE : Timeout or repeat signal
uint8_t InfraredRec::readFrame(uint8_t*buf, bool timeout){
	uint16_t length0;
	uint16_t length1;
	uint16_t lengthStop;
	uint8_t data=0;
	uint8_t byte=0;
	uint8_t b=0;
	
	uint32_t p = receivePulse(timeout);
	if(p==0xFFFF){
		return 0xFE;
	}
	
	format = checkFormat(p);
	if(checkRepeat(format, p)){
		return(0xFE);
	}
	
	switch(format){
	case formatAEHA:
		length0=42;
		length1=127;
		lengthStop=200;
		break;
	case formatNEC:
		length0=56;
		length1=169;
		lengthStop=260;
		break;
	default:
		return 0xFF;
	}
	
	while(1){
		p = receivePulse(true);
		// Timeout
		if(p==0xFFFF){
			break;
		}
		
		p = p>>16;	// OFF length
		if((length0*0.5) < p && (length0*1.5) > p){
			;
		}else if((length1*0.5) < p && (length1*1.5) > p){
			data = data | (1<<b);	// LSB first
		}else if(lengthStop < p){
			break;
		}
		b++;
		
		// Final bit of 1 byte
		if(b==8){
			buf[byte] = data;
			data=0;
			b=0;
			byte++;
			
			if(byte>=maxFrameSize){
				return byte;
			}
		}
	}
	return byte;
}


//---------------------------------
// Public Class Function

InfraredRec::InfraredRec(uint8_t setGPIO){
	recGPIO = setGPIO;
	pullUpDnControl(recGPIO, PUD_OFF);
	pinMode(recGPIO, INPUT);

	format = formatUnknown;
	frameCount = 0;
}


// Read data from receiver
void InfraredRec::readData(){
	for(uint8_t c = 0; c<maxFrameCount; c++){
		if(c==0){
			frameSize[c] = readFrame(frameData[c],false);	// 1st frame no timeout
		}else{
			frameSize[c] = readFrame(frameData[c],true);
		}

		// Timeout or non supported format
		if(frameSize[c] == 0xFF || frameSize[c] == 0xFE){
			return;
		}

		frameCount = c+1;
	}
}


