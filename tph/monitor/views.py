"""
Views contoroller.

@date 27 November 2019
@author mitsuhisaT <asihustim@gmail.com>
"""
from importlib import import_module
import logging
import deprecation
from datetime import timedelta
from django.conf import settings as ts
from django.http import JsonResponse, HttpResponse, Http404
from django.shortcuts import render
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView
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
    context = {
        'site_title': 'TPH monitor',
        'title': 'Show current environment:pressure, humidity and temperature',
        'bme280dcs': bme280dcs,
        'year': 2019,
        'owner': ts.OWNER,
    }
    # https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/#render
    return render(request, 'monitor/show.html', context)


def __response(request, bme280s, title):
    """Show datas from BME280."""
    logger.debug('start')
    logger.debug(f'length bme280s: {len(bme280s)}')
    context = {
        'site_title': 'TPH monitor',
        'title': title,
        'page_obj': bme280s,
        'year': 2019,
        'owner': ts.OWNER,
    }
    # https://docs.djangoproject.com/en/3.0/topics/http/shortcuts/#render
    return render(request, 'monitor/bme280.html', context)


@csrf_exempt
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


class Bme280List(ListView):
    """For list view."""

    model = BME280
    paginate_by = ts.PAGE_SIZE
    template_name = 'monitor/bme280.html'
    title = f'Show pressure, humidity and temperature'

    def get_context_data(self, **kwargs):
        """Get context data."""
        context = super().get_context_data(**kwargs)
        context['site_title'] = 'TPH monitor'
        context['title'] = self.title
        context['year'] = '2019-2020'
        context['owner'] = ts.OWNER
        return context

    def get_queryset(self):
        """Year, month, day."""
        if 'year' in self.kwargs:
            year = self.kwargs['year']
            if 'month' in self.kwargs:
                month = self.kwargs['month']
                if 'day' in self.kwargs:
                    day = self.kwargs['day']
                    self.title = f'Show {year}/{month}/{day} pressure, humidity and temperature'
                    return BME280.objects.filter(measure_date__year=year,
                                                 measure_date__month=month,
                                                 measure_date__day=day,
                                                )
                else:
                    self.title = f'Show {year}/{month} pressure, humidity and temperature'
                    return BME280.objects.filter(measure_date__year=year,
                                                 measure_date__month=month,
                                                )
            else:
                self.title = f'Show {year} pressure, humidity and temperature'
                return BME280.objects.filter(measure_date__year=year)
        return BME280.objects.all()


class BME280ViewSet(viewsets.ModelViewSet):
    """API endpoint that allows BME280 to be viewed and edit."""

    queryset = BME280.objects.all().order_by('-pub_date')
    serializer_class = BME280Serializer
