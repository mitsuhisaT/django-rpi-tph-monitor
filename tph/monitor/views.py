"""
Views contoroller.

@date 27 November 2019
@author mitsuhisaT <asihustim@gmail.com>
"""
import logging
from django.shortcuts import render
from django.http import HttpResponse, Http404
# from .bme280i2c import BME280I2C
from .bme280i2c_stub import BME280I2C
import tph.settings as ts

logger = logging.getLogger(__name__)


def index(request):
    """Index page."""
    return HttpResponse("Hello, world. You're at the tph/monitor index.")


def show(request):
    """Show current environment pressure, humidity and temperature."""
    logger.debug('start')
    bme280i2c = BME280I2C(ts.BME280CH1_ADDR)
    if not bme280i2c.meas():
        logger.warn("Can't get datas from BME280")
        raise Http404("Can't get datas from BME280")
    logger.debug('end')
    return render(request, 'monitor/show.html', {
        'site_title': 'TPH monitor',
        'title': 'Show current environment:pressure, humidity and temperature',
        'pressure': f'{bme280i2c.P:+4.2f}',
        'humidity': f'{bme280i2c.H:+3.2f}',
        'temperature': f'{bme280i2c.T:+3.2f}',
        'year': 2019,
        'owner': ts.OWNER,
    })


def bsstest(request, bss_id):
    response = "You're in Bootstrap Sass test page: bssid %s."
    HttpResponse(response % bss_id)
