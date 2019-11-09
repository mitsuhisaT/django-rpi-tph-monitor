
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
#include "InfraredRec.h"


//---------------------------------
// Function

int main(int argc, char *argv[]){

	if(wiringPiSetupGpio() == -1){
		printf("Init Error\n");
		return 1;
	}

	InfraredLED iled(13);
	InfraredRec rec(4);

	// Read data from receiver
	printf("Waiting for signal...\n");
	rec.readData();
	
	switch(rec.format){
	case InfraredRec::formatAEHA:
		printf("AEHA format\n");
		break;
	case InfraredRec::formatNEC:
		printf("NEC format\n");
		break;
	case InfraredRec::formatSONY:
		printf("SONY format\n");
		return 0;
	default:
		printf("Unknown format\n");
		return 0;
	}
	printf("Frame Count : %d\n", rec.frameCount);
	for(int i=0; i<rec.frameCount; i++){
		printf("Frame#%d Size:%d\n",i,rec.frameSize[i]);
		printf("Data:");
		for(int j=0; j<rec.frameSize[i]; j++){
			printf("0x%02x",rec.frameData[i][j]);
			if(j!=rec.frameSize[i]-1){
				printf(",");
			}
		}
		printf("\n");
	}

	delay(5000);

	// Send received data from LED
	printf("Sending data from LED...\n");
	for(int i=0; i<rec.frameCount; i++){
		iled.sendFrame(rec.format, rec.frameData[i], rec.frameSize[i]);
	}

	return 0;
}
