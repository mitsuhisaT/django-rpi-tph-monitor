#!/usr/bin/env python3

import RPi.GPIO as GPIO
import time

# GPIOの準備
GPIO.setmode(GPIO.BCM)

# SW1, SW2, SW3ピン入力設定
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

# LED D4, D5ピン出力設定
GPIO.setup(5, GPIO.OUT)
GPIO.setup(6, GPIO.OUT)

try:
    while True:
        # SW1かSW3が押された場合
        if 0==GPIO.input(22) or 0==GPIO.input(24):
            # D4点灯
            GPIO.output(5, 1)
        else:
            # D4消灯
            GPIO.output(5, 0)

        # SW2かSW3が押された場合
        if 0==GPIO.input(23) or 0==GPIO.input(24):
            # D5点灯
            GPIO.output(6, 1)
        else:
            # D5消灯
            GPIO.output(6, 0)

        time.sleep(0.01)

# Ctrl+Cが押されたらGPIOを解放
except KeyboardInterrupt:
    GPIO.cleanup(5)
    GPIO.cleanup(6)
    GPIO.cleanup(22)
    GPIO.cleanup(23)
    GPIO.cleanup(24)




