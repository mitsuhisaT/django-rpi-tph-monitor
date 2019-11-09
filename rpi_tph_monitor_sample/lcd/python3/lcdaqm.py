#!/usr/bin/env python3

"""
LCD AQM0802A-RN-GBW Control Module via I2C
 2017/10/22
"""

import smbus
import time

class LCDAQM:
    def __init__(self):
        self.i2c_addr = 0x3E
        self.i2c = smbus.SMBus(1)
        self.count = 0  # Count number of character in current line
        self.line = 1   # Current line number

    # I2C write one byte data to addr
    def write_address_onebyte(self, addr, data):
        data_list = [data]
        try:
            self.i2c.write_i2c_block_data(self.i2c_addr, addr, data_list)
        except IOError:
            return False

        time.sleep(50/1000000)

        return True

    # Initialize LCD
    def init_lcd(self):
        self.write_address_onebyte(0, 0x38)
        self.write_address_onebyte(0, 0x39)
        self.write_address_onebyte(0, 0x14)
        self.write_address_onebyte(0, 0x70)
        self.write_address_onebyte(0, 0x56)
        self.write_address_onebyte(0, 0x6C)
        time.sleep(0.25)
        self.write_address_onebyte(0, 0x38)
        self.write_address_onebyte(0, 0x0C)
        self.clear();

    # Print string on LCD
    def print(self, str):
        chars = list(str)
        for i in range(len(chars)):
            self.count += 1
            if self.count > 8:
                if self.line==2:
                    home()
                else:
                    sec_line()
            self.write_address_onebyte(0x40, ord(chars[i]))

    # Clear LCD and return to home
    def clear(self):
        self.count = 0
        self.line = 1
        self.write_address_onebyte(0, 0x1)
        time.sleep(0.002)

    # Return to home without deleting characters
    def home(self):
        self.count = 0
        self.line = 1
        self.write_address_onebyte(0, 0x2)
        time.sleep(0.002)

    # Go to second line
    def sec_line(self):
        self.count = 0
        self.line = 2
        self.write_address_onebyte(0, 0xC0)


def main():
    lcd = LCDAQM()
    lcd.init_lcd()

    lcd.print('AQM0802')
    time.sleep(1)
    lcd.clear()
    time.sleep(1)
    lcd.print('Test')
    time.sleep(1)
    lcd.sec_line()
    lcd.print('Success')
    time.sleep(1)

if __name__ == '__main__':
    main()


