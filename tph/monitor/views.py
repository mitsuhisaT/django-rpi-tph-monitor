"""
Views contoroller.

@date 27 November 2019
@author mitsuhisaT <asihustim@gmail.com>
"""
from importlib import import_module
import logging
from datetime import timedelta
from django.conf import settings as ts
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
from rest_framework import viewsets
from monitor.data_container import BME280dc
from monitor.store_tph_bg import bgStoreTph
from monitor.models import BME280
from monitor.serializers import BME280Serializer
if ts.ON_RASPBERRY_PI:
    module_object = import_module('monitor.bme280i2c')
else:
    module_object = import_module('monitor.bme280i2c_stub')
BME280I2C = getattr(module_object, 'BME280I2C')

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
    bme280dcs = []
    for i in range(5):
        if not bme280i2c.meas():
            logger.warn("Can't get datas from BME280")
            raise Http404("Can't get datas from BME280")
        logger.debug('end')
        bme280dcs.append(BME280dc(t=bme280i2c.T, p=bme280i2c.P, h=bme280i2c.H))
    return render(request, 'monitor/show.html', {
        'site_title': 'TPH monitor',
        'title': 'Show current environment:pressure, humidity and temperature',
        'bme280dcs': bme280dcs,
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


class BME280ViewSet(viewsets.ModelViewSet):
    """API endpoint that allows BME280 to be viewed and edit."""
    queryset = BME280.objects.all().order_by('-measure_datetime')
    serializer_class = BME280Serializer
