#!/usr/bin/env python3

"""
Measure pressure, humidity and temperature from BME280 and store them.

Add store data into database, add logging and modified comment.

Original code get from
https://www.indoorcorgielec.com/wp-content/uploads/products/rpi-tph-monitor-rev2/bme280i2c.zip

For more information to RPi TPH Monitor Rev2.
https://www.indoorcorgielec.com/products/rpi-tph-monitor-rev2/
About smbus2
https://pypi.org/project/smbus2/
https://github.com/kplindegaard/smbus2

About smbus(SMBus)
https://github.com/bivab/smbus-cffi
"""
import logging
import time
from importlib import import_module
from django.conf import settings as ts
from django.utils import timezone
from monitor.lcd import LCDAQM
if ts.USE_SMBUS2:
    module_object = import_module('smbus2')
else:
    module_object = import_module('smbus')
SMBus = getattr(module_object, 'SMBus')


logger = logging.getLogger(__name__)


class BME280I2C:
    """
    Measure pressure, humidity and temperature from BME280 and store them.

    BME280 detail to see
        https://www.bosch-sensortec.com/bst/products/all_products/bme280

    """

    @staticmethod
    def get_signed8(uint: int) -> int:
        """
        Return signed int from 8bit uint.

        Params
            unit (int): unsigned integer

        Returns:
            unit (int): signed integer

        """
        if uint > 127:
            return uint - 256
        return uint

    @staticmethod
    def get_signed16(uint: int) -> int:
        """
        Return signed int from 16bit uint.

        Params
            unit (int): unsigned integer

        Returns:
            unit (int): signed integer

        """
        if uint > 32767:
            return uint - 65536
        return uint

    def __init__(self, i2c_addr):
        """Define I2C address 0x76 or 0x77."""
        self.i2c_addr = i2c_addr
        self.i2c = SMBus(1)
        self.cal = {}               # Calibration data
        self.adc_T = 0
        self.adc_P = 0
        self.adc_H = 0
        self.T = 0
        self.P = 0
        self.H = 0
        self.t_fine = 0

    @property
    def T(self):
        """Get T(temperature)."""
        return self.__T

    @T.setter
    def T(self, T):
        """Set T(temperature)."""
        self.__T = T

    @property
    def P(self):
        """Get P(pressure)."""
        return self.__P

    @P.setter
    def P(self, P):
        """Set P(pressure)."""
        self.__P = P

    @property
    def H(self):
        """Get H(humidity)."""
        return self.__H

    @H.setter
    def H(self, H):
        """Set H(humidity)."""
        self.__H = H

    def read_address(self, addr, length):
        """I2C read length byte from addr."""
        try:
            return self.i2c.read_i2c_block_data(self.i2c_addr, addr, length)
        except IOError:
            return [0 for i in range(length)]

    def read_address_twobyte(self, addr):
        """I2C read 2 byte from addr."""
        data = self.i2c.read_i2c_block_data(self.i2c_addr, addr, 2)
        return data[0] + (data[1] << 8)

    def write_address(self, addr, data):
        """I2C write data to addr."""
        self.i2c.write_i2c_block_data(self.i2c_addr, addr, data)

    def id_read(self):
        """Read BME280 ID and return True if success."""
        data = self.read_address(0xD0, 1)
        if data[0] == 0x60:
            return True
        return False

    def status_read(self):
        """Read status."""
        data = self.read_address(0xF3, 1)
        return data[0] & 0x9

    def read_cal(self) -> None:
        """Read calibration registers and store in cal dict."""
        self.cal['dig_T1'] = self.read_address_twobyte(0x88)
        self.cal['dig_T2'] = self.get_signed16(self.read_address_twobyte(0x8A))
        self.cal['dig_T3'] = self.get_signed16(self.read_address_twobyte(0x8C))
        self.cal['dig_P1'] = self.read_address_twobyte(0x8E)
        self.cal['dig_P2'] = self.get_signed16(self.read_address_twobyte(0x90))
        self.cal['dig_P3'] = self.get_signed16(self.read_address_twobyte(0x92))
        self.cal['dig_P4'] = self.get_signed16(self.read_address_twobyte(0x94))
        self.cal['dig_P5'] = self.get_signed16(self.read_address_twobyte(0x96))
        self.cal['dig_P6'] = self.get_signed16(self.read_address_twobyte(0x98))
        self.cal['dig_P7'] = self.get_signed16(self.read_address_twobyte(0x9A))
        self.cal['dig_P8'] = self.get_signed16(self.read_address_twobyte(0x9C))
        self.cal['dig_P9'] = self.get_signed16(self.read_address_twobyte(0x9E))
        self.cal['dig_H1'] = self.read_address(0xA1, 1)[0]
        self.cal['dig_H2'] = self.get_signed16(self.read_address_twobyte(0xE1))
        self.cal['dig_H3'] = self.read_address(0xE3, 1)[0]
        self.cal['dig_H4'] = self.get_signed16(
                                (self.read_address(0xE4, 1)[0] << 4)
                                + (self.read_address(0xE5, 1)[0] & 0xF))
        self.cal['dig_H5'] = self.get_signed16(
                                self.read_address_twobyte(0xE5) >> 4)
        self.cal['dig_H6'] = self.get_signed8(self.read_address(0xE7, 1)[0])

    def print_cal(self):
        for k, v in sorted(self.cal.items(), key=lambda x: x[0]):
            print(f' {k} : {v}')

    def forced(self):
        """
        Measure sensor data and store in adc_T, adc_P and adc_H.

        0xF5, [0x00]: config
        0xF2, [0x05]: ctrl_hum, oversampling x16
        0xF4, [0xB5]: ctrl_meas, oversampling x16, forced mode
        """
        self.write_address(0xF5, [0x0])
        self.write_address(0xF2, [0x5])
        self.write_address(0xF4, [0xB5])

        while self.status_read() is False:
            time.sleep(0.001)

        data = self.read_address(0xF7, 8)
        self.adc_P = (data[0] << 12) + (data[1] << 4) + (data[2] >> 4)
        self.adc_T = (data[3] << 12) + (data[4] << 4) + (data[5] >> 4)
        self.adc_H = (data[6] << 8) + data[7]

    def comp_T(self):
        """Calculate temp from adc_T and calibration data."""
        var1 = ((((self.adc_T >> 3) - (self.cal['dig_T1'] << 1)))
                * (self.cal['dig_T2'])) >> 11
        var2 = (((((self.adc_T >> 4) - (self.cal['dig_T1']))
                  * ((self.adc_T >> 4) - (self.cal['dig_T1']))) >> 12)
                * (self.cal['dig_T3'])) >> 14
        self.t_fine = var1 + var2
        self.T = ((self.t_fine * 5 + 128) >> 8) / 100

    def comp_P(self):
        """Calculate pressure from adc_P and calibration data."""
        var1 = self.t_fine - 128000
        var2 = (var1 * var1 * self.cal['dig_P6']
                + ((var1 * self.cal['dig_P5']) << 17)
                + (self.cal['dig_P4'] << 35))
        var1 = (((var1 * var1 * self.cal['dig_P3']) >> 8)
                + ((var1 * self.cal['dig_P2']) << 12))
        var1 = (((1 << 47) + var1)) * (self.cal['dig_P1']) >> 33
        if var1 == 0:
            return

        p = 1048576 - self.adc_P
        p = (((p << 31) - var2) * 3125) // var1
        var1 = (self.cal['dig_P9'] * (p >> 13) * (p >> 13)) >> 25
        var2 = (self.cal['dig_P8'] * p) >> 19
        p = ((p + var1 + var2) >> 8) + ((self.cal['dig_P7']) << 4)
        self.P = p/25600

    def comp_H(self):
        """Calculate humidity from adc_H and calibration data."""
        v_x1_u32r = (self.t_fine - 76800)
        v_x1_u32r = (
                    (((((self.adc_H << 14)
                        - ((self.cal['dig_H4']) << 20)
                        - ((self.cal['dig_H5']) * v_x1_u32r)) + 16384) >> 15)
                        * (
                        ((((((v_x1_u32r * self.cal['dig_H6']) >> 10)
                            * (((v_x1_u32r * self.cal['dig_H3']) >> 11)
                                + 32768)) >> 10) + 2097152)
                            * self.cal['dig_H2'] + 8192) >> 14)))
        v_x1_u32r = (v_x1_u32r - (
                    ((((v_x1_u32r >> 15) * (v_x1_u32r >> 15)) >> 7)
                        * self.cal['dig_H1']) >> 4))
        if v_x1_u32r < 0:
            v_x1_u32r = 0
        if v_x1_u32r > 419430400:
            v_x1_u32r = 419430400
        self.H = (v_x1_u32r >> 12) / 1024

    def meas(self):
        """Measure T/P/H and output T/H,P to LCD."""
        if not self.id_read():
            return False
        self.read_cal()
        self.forced()
        self.comp_T()
        self.comp_P()
        self.comp_H()
        self.i2c.close()

        lcd = LCDAQM()
        lcd.init_lcd()
        lcd.clear()
        lcd.print(timezone.localtime().strftime('%m%d%H%M'))
        lcd.sec_line()
        if ts.LCD_DISP_TPH == 'P':
            lcd.print(f'{self.P:.1f}')
        else:
            lcd.print(f'{self.T:.1f},{self.H:.0f}')
        lcd.close()

        return True

    def print_reg(self):
        print(f' t_fine : {self.t_fine}')
        print(f' adc_T  : {self.adc_T}')
        print(f' adc_P  : {self.adc_P}')
        print(f' adc_H  : {self.adc_H}')

    def print_meas(self):
        print(' Temp     : {:.1f}C'.format(self.T))
        print(' Pressure : {:.1f}hPa'.format(self.P))
        print(' Humidity : {:.1f}%'.format(self.H))


# RPi TPH Monitor addresses.
BME280CH1_ADDR = 0x76
BME280CH2_ADDR = 0x77
def main():
    bme280ch1 = BME280I2C(BME280CH1_ADDR)
    bme280ch2 = BME280I2C(BME280CH2_ADDR)

    if bme280ch1.meas():
        print('BME280 0x76')
        bme280ch1.print_cal()
        bme280ch1.print_reg()
        bme280ch1.print_meas()

    if bme280ch2.meas():
        print('BME280 0x77')
        bme280ch2.print_cal()
        bme280ch2.print_reg()
        bme280ch2.print_meas()


if __name__ == '__main__':
    main()
