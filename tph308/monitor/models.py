"""Models definition."""
from django.db import models
from django.utils import timezone


class BME280(models.Model):
    """Store from BME280 sensor.

    Store from BME280 sensor.
    BME280 senses pressure, humidity and temperature.

    Sees:
        https://www.bosch-sensortec.com/bst/products/all_products/bme280
        https://www.indoorcorgielec.com/products/rpi-tph-monitor-rev2/

    """

    pressure = models.FloatField()
    humidity = models.FloatField()
    temperature = models.FloatField()
    measure_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['measure_date']

    def ___str___(self):
        """About this BME2880 Model."""
        return 'Store pressure, humidity and temperature.'
