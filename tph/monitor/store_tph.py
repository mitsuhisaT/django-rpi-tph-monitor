#!/usr/bin/env python3
"""
Store temperature, pressure and humidity from BME230I2C.
"""
from datetime import datetime
import logging
from django.utils import timezone
# from bme280i2c import BME280I2C
from .bme280i2c_stub import BME280I2C
from .data_container import BME280dc
from .models import BME280

logger = logging.getLogger(__name__)


class StoreTph():
    """Store temperature, pressure and humidity get from BME230I2C."""

    def __init__(self, i2c_addr):
        """Constractor."""
        logger.debug('start')
        self.__bme280i2c = BME280I2C(i2c_addr)
        self.__i2c_addr = i2c_addr
        self.__bme280dc = BME280dc(t=0.0, p=0.0, h=0.0)
        logger.debug('end')

    def __getTPH(self):
        """Get temperature, pressure and humidity from BME230I2C."""
        logger.debug('start')
        if self.__bme280i2c.meas():
            self.__bme280dc.t = self.__bme280i2c.T
            self.__bme280dc.p = self.__bme280i2c.P
            self.__bme280dc.h = self.__bme280i2c.H
            logger.debug('end')
            return True
        else:
            self.__bme280dc.t = 0.0
            self.__bme280dc.p = 0.0
            self.__bme280dc.h = 0.0
            logger.critical("Can't measure from BME280I2C.")
            logger.debug('end, errore')
            return False

    def save(self):
        """Store temperature, pressure and humidity into BME280."""
        logger.debug('start')
        if self.__getTPH():
            bme280 = BME280(
                            temperature=self.__bme280dc.t,
                            pressure=self.__bme280dc.p,
                            humidity=self.__bme280dc.h,
                            )
            print(repr(bme280))
            bme280.save()
            logger.debug('end')
            return bme280.id
        else:
            logger.woarn("Can't get datas from BMC280I2C.")
            # TODO exception
            return False

    def saveData(self, bme280dc):
        """Store designated datas."""
        logger.debug('start')
        BME280(
            temperature=bme280dc.t,
            pressure=bme280dc.p,
            humidity=bme280dc.h,
            measure_datetime=bme280dc.mdt,
        ).save()
        logger.debug('end')

    def betweenDatetime(self, bdt: datetime, edt: datetime):
        """
        Get BME280s between begin datetime and end datetime.

        Params:
            bdt (datetime): bigin datetime
            edt (datetime): end datetime

        Returns:
            BME280: stored temperature, pressure, humidity adn datetime

        """
        logger.debug('start')
        logger.debug('end')
        return BME280.objects.filter(
                                     measure_datetime__lte=bdt,
                                     measure_datetime__gte=edt,
                                    ).values()
# 
# 
# def main():
#     logger.debug('test store.')
# 
#     # from django.conf import settings
#     # settings.configure()
# 
#     storeTph = StoreTph(0x76)
#     storeTph.save()
#     logger.debug('end.')
# 
# 
# if __name__ == '__main__':
#     main()
