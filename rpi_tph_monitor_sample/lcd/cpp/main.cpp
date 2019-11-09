
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
// Constant
#define STRLENGTH 256

//---------------------------------
// Function

int main(int argc, char *argv[]){
	if(wiringPiSetupGpio() == -1){
		return 1;
	}

	// LED and SW setting
	pinMode(5, OUTPUT);
	pinMode(6, OUTPUT);
	pinMode(22, INPUT);
	pullUpDnControl(22, PUD_UP);
	pinMode(23, INPUT);
	pullUpDnControl(23, PUD_UP);
	pinMode(24, INPUT);
	pullUpDnControl(24, PUD_UP);

	// LCD initialize
	LCDAQM lcd;
	lcd.init();
	char str[STRLENGTH];

	strcpy(str, "Test");
	lcd.printStr(str);
	delay(1000);
	strcpy(str, "Start");
	lcd.secLine();
	lcd.printStr(str);

	while(1){
		// SW1
		if(0==digitalRead(22)){
			digitalWrite(5, 1);
		}else{
			digitalWrite(5, 0);
		}

		// SW2
		if(0==digitalRead(23)){
			digitalWrite(6, 1);
		}else{
			digitalWrite(6, 0);
		}
	}

	return 0;
}
