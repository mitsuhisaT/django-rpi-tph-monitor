"""Models definition."""
from django.db import models


class BME280(models.Model):
    """Store from BME280 sensor.

    Store from BME280 sensor.
    BME280 senses pressure, humidity and temperature.

    See https://www.bosch-sensortec.com/bst/products/all_products/bme280

    """

    pressure = models.FloatField()
    humidity = models.FloatField()
    temperature = models.FloatField()
    measure_datetime = models.DateTimeField(auto_now_add=True)
