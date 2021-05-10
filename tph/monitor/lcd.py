"""
Controle LCD Class for the RPi TPH Monitor Rev2.

For more information to RPi TPH Monitor Rev2.
https://www.indoorcorgielec.com/products/rpi-tph-monitor-rev2/
"""

import time
from importlib import import_module
from django.conf import settings as ts
if ts.USE_SMBUS2:
    module_object = import_module('smbus2')
else:
    module_object = import_module('smbus')
SMBus = getattr(module_object, 'SMBus')


class LCDAQM:
    """
    Controle LCD Class for the RPi TPH Monitor Rev2.

    Attributes:
        i2c_addr (): I2C address.
        i2c (obj): ls /dev/i2c* -> /dev/i2c-1 then SMBus(1)
        count (int): Count number of character in current line
        line (int): Current line number
    """

    def __init__(self):
        self.i2c_addr = 0x3E
        self.i2c = SMBus(1)
        self.count = 0
        self.line = 1

    def write_address_onebyte(self, addr, data):
        """
        I2C write one byte data to addr.

        Args:
            addr (int): Start register.
            data (byte): character of byte.

        Returns:
            result write data.
            True: success.
            False: IOError.

        Raises:
            None
        """
        data_list = [data]
        try:
            self.i2c.write_i2c_block_data(self.i2c_addr, addr, data_list)
        except IOError:
            return False

        time.sleep(50/1000000)

        return True

    def init_lcd(self):
        """
        Initialize LCD.
        """
        self.write_address_onebyte(0, 0x38)
        self.write_address_onebyte(0, 0x39)
        self.write_address_onebyte(0, 0x14)
        self.write_address_onebyte(0, 0x70)
        self.write_address_onebyte(0, 0x56)
        self.write_address_onebyte(0, 0x6C)
        time.sleep(0.25)
        self.write_address_onebyte(0, 0x38)
        self.write_address_onebyte(0, 0x0C)
        self.clear()

    def print(self, str):
        """
        Print string on LCD.

        Args:
            str (): string for output LCD.
        """
        chars = list(str)
        for i in range(len(chars)):
            self.count += 1
            if self.count > 8:
                if self.line == 2:
                    self.home()
                else:
                    self.sec_line()
            self.write_address_onebyte(0x40, ord(chars[i]))

    def clear(self):
        """
        Clear LCD and return to home.
        """
        self.count = 0
        self.line = 1
        self.write_address_onebyte(0, 0x1)
        time.sleep(0.002)

    def home(self):
        """
        Return to home without deleting characters.
        """
        self.count = 0
        self.line = 1
        self.write_address_onebyte(0, 0x2)
        time.sleep(0.002)

    def sec_line(self):
        """
        Go to second line.
        """
        self.count = 0
        self.line = 2
        self.write_address_onebyte(0, 0xC0)

    def close(self):
        """
        Close SMBus.
        """
        self.i2c.close()


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
