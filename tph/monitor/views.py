"""
Views contoroller.

@date 27 November 2019
@author mitsuhisaT <asihustim@gmail.com>
"""
import csv
from importlib import import_module
from io import StringIO
import logging
import deprecation
from datetime import timedelta
from django.conf import settings as ts
from django.core.files import File
from django.http import JsonResponse, HttpResponse, Http404
from django.http import StreamingHttpResponse
# from django.template import loader
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
# from django.views.generic import ListView
# from rest_framework import viewsets
# from monitor import csv
from monitor import model_csv_download as dl
from monitor.data_container import BME280dc
from monitor.store_tph_bg import bgStoreTph
from monitor.models import BME280
# from monitor.serializers import BME280Serializer
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
def current_tph(request):
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
    context = {
        'site_title': 'TPH monitor',
        'title': 'Show current environment:pressure, humidity and temperature',
        'bme280dcs': bme280dcs,
        'year': ts.COPYRIGHT_YEAR,
        'owner': ts.OWNER,
    }
    # https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/#render
    return render(request, 'monitor/show.html', context)


@deprecation.deprecated(deprecated_in="1.0", removed_in="2.0",
                        # current_version=__version__,
                        details="Use the Bme280List class instead")
def __response(request, bme280s, title):
    """Show datas from BME280."""
    logger.debug('start')
    logger.debug(f'length bme280s: {len(bme280s)}')
    context = {
        'site_title': 'TPH monitor',
        'title': title,
        'page_obj': bme280s,
        'year': ts.COPYRIGHT_YEAR,
        'owner': ts.OWNER,
    }
    # https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/#render
    return render(request, 'monitor/bme280.html', context)


@csrf_exempt
@deprecation.deprecated(deprecated_in="1.0", removed_in="2.0",
                        # current_version=__version__,
                        details="Use the Bme280List class instead")
def showlastmonth(request):
    """Show last month environment pressure, humidity and temperature."""
    logger.debug('start')
    tMonth = timezone.now().replace(day=1)
    lMonth = tMonth - timedelta(days=1)
    bme280s = BME280.objects.filter(measure_date__month=lMonth.month)
    title = 'Show last month pressure, humidity and temperature'
    return __response(request, bme280s, title)


@csrf_exempt
@deprecation.deprecated(deprecated_in="1.0", removed_in="2.0",
                        # current_version=__version__,
                        details="Use the Bme280List class instead")
def showmonth(request, year: int, month: int):
    """Show year/month environment pressure, humidity and temperature."""
    logger.debug(f'start, year: {year}, month: {month}')
    bme280s = BME280.objects.filter(measure_date__year=year,
                                    measure_date__month=month,
                                    )
    title = f'Show {year}/{month} pressure, humidity and temperature'
    return __response(request, bme280s, title)


@csrf_exempt
@deprecation.deprecated(deprecated_in="1.0", removed_in="2.0",
                        # current_version=__version__,
                        details="Use the Bme280List class instead")
def showday(request, year: int, month: int, day: int):
    """Show year/month/day environment pressure, humidity and temperature."""
    logger.debug(f'start, year: {year}, month: {month}, day: {day}')
    bme280s = BME280.objects.filter(measure_date__year=year,
                                    measure_date__month=month,
                                    measure_date__day=day,
                                    )
    title = f'Show {year}/{month}/{day} pressure, humidity and temperature'
    return __response(request, bme280s, title)


def bme280_csv_dl(request):
    """
    """
    qs = BME280.objects.all()
    # lookups = dl.get_lookup_fields(qs.model)
    # output order.
    lookups = [
        'id',
        'measure_date',
        'temperature',
        'pressure',
        'humidity',
    ]
    dataset = dl.qs2dataset(qs, fields=lookups)
    fp = StringIO()
    writer = csv.DictWriter(fp, fieldnames=lookups)
    writer.writeheader()
    for data_item in dataset:
        writer.writerow(data_item)
    stream_file = File(fp)
    return StreamingHttpResponse(
        stream_file,
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="bme280.csv"'},
    )


# @api_view(['POST', 'GET'])
@csrf_exempt
def tasks(request, rpt, untl):
    """Register background tasks."""
    logger.debug('start')
    if request.method == 'GET':
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
# 
# 
# class BME280ViewSet(viewsets.ModelViewSet):
#     """API endpoint that allows BME280 to be viewed and edit."""
# 
#     queryset = BME280.objects.all().order_by('-measure_date')
#     serializer_class = BME280Serializer
