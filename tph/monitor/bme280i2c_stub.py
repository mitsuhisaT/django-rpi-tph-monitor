#!/usr/bin/env python3

"""
Measure pressure, humidity and temperature from BME280 and store them.

Add store data into database, add logging and modified comment.

Original code get from
https://www.indoorcorgielec.com/wp-content/uploads/products/rpi-tph-monitor-rev2/bme280i2c.zip

For more information to RPi TPH Monitor Rev2.
https://www.indoorcorgielec.com/products/rpi-tph-monitor-rev2/
"""

import logging
import random

logger = logging.getLogger(__name__)

# RPi TPH Monitor addresses.
BME280CH1_ADDR = 0x76
BME280CH2_ADDR = 0x77


class BME280I2C:
    """
    Measure pressure, humidity and temperature from BME280 and store them.

    BME280 detail to see
        https://www.bosch-sensortec.com/bst/products/all_products/bme280

    """

    def __init__(self, i2c_addr):
        """Define I2C address 0x76 or 0x77."""
        self.i2c_addr = i2c_addr
        self.i2c = None  # smbus.SMBus(1)
        self.cal = {}               # Calibration data
        self.adc_T = 0
        self.adc_P = 0
        self.adc_H = 0
        self.T = 0
        self.P = 0
        self.H = 0
        self.t_fine = 0

    def print_cal(self):
        cal_dummys = [
            {'k': '0x01', 'v': 23},
        ]
        # FIXME
        for k, v in sorted(cal_dummys):
            print(f' {k} : {v}')

    def forced(self):
        """
        Measure sensor data and store in adc_T, adc_P and adc_H.

        0xF5, [0x00]: config
        0xF2, [0x05]: ctrl_hum, oversampling x16
        0xF4, [0xB5]: ctrl_meas, oversampling x16, forced mode
        """
        self.adc_P = random.randint(524000, 524288)
        self.adc_T = random.randint(524000, 524288)
        self.adc_H = random.randint(32700, 32768)

    def comp_T(self):
        """Calculate temp from adc_T and calibration data."""
        self.t_fine = random.randint(111000, 112000)
        self.T = random.uniform(-30, 50)

    def comp_P(self):
        """Calculate pressure from adc_P and calibration data."""
        self.P = random.uniform(800, 1200)

    def comp_H(self):
        """Calculate humidity from adc_H and calibration data."""
        self.H = random.uniform(0, 100)

    def meas(self):
        """Measure T/P/H."""
        if self.i2c_addr == BME280CH1_ADDR:
            # self.read_cal()
            self.forced()
            self.comp_T()
            self.comp_P()
            self.comp_H()
            return True
        else:
            return False

    def print_reg(self):
        print(f' t_fine : {self.t_fine}')
        print(f' adc_T  : {self.adc_T}')
        print(f' adc_P  : {self.adc_P}')
        print(f' adc_H  : {self.adc_H}')

    def print_meas(self):
        print(' Temp     : {:.1f}C'.format(self.T))
        print(' Pressure : {:.1f}hPa'.format(self.P))
        print(' Humidity : {:.1f}%'.format(self.H))


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
