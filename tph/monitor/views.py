"""
Views contoroller.

@date 27 November 2019
@author mitsuhisaT <asihustim@gmail.com>
"""
import logging
from datetime import timedelta
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .bme280i2c import BME280I2C
from .bme280i2c_stub import BME280I2C
from .store_tph_bg import bgStoreTph
import tph.settings as ts

logger = logging.getLogger(__name__)


def index(request):
    """Index page."""
    return HttpResponse("Hello, world. You're at the tph/monitor index.")


# @api_view(['GET'])
@csrf_exempt
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


# @api_view(['POST'])
@csrf_exempt
def tasks(request, rpt, untl):
    """Register background tasks."""
    logger.debug('start')
    if request.method == 'POST':
        end_datetime = timezone.now() + timedelta(seconds=untl)
        bgStoreTph(repeat=rpt,
                   repeat_until=end_datetime)
        resJson = {'status': True,
                   'repeat': rpt,
                   'run_at': timezone.now(),
                   'repeat_until': end_datetime
                   }
        logger.debug('end')
        return JsonResponse(resJson, status=302)
    else:
        logger.debug('end, status: 405')
        return JsonResponse({'status': False}, status=405)


# @api_view(['GET'])
@csrf_exempt
def bsstest(request, bss_id):
    response = "You're in Bootstrap Sass test page: bssid %s."
    HttpResponse(response % bss_id)
