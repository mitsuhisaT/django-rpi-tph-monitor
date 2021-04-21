"""
Views contoroller.

@date 30 January 2020
@author mitsuhisaT <asihustim@gmail.com>
"""
import logging
from django.conf import settings as ts
from django.views.generic import ListView
from monitor.models import BME280

logger = logging.getLogger(__name__)


class Bme280List(ListView):
    """For list view."""

    model = BME280
    paginate_by = ts.PAGE_SIZE
    template_name = 'monitor/bme280.html'
    title = 'all'

    def get_context_data(self, **kwargs):
        """Get context data."""
        context = super().get_context_data(**kwargs)
        context['site_title'] = 'TPH monitor'
        context['title'] = self.title
        context['year'] = ts.COPYRIGHT_YEAR
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
                    self.title = f'{year}/{month}/{day}'
                    logger.debug(f'{self.title}')
                    return BME280.objects.filter(measure_date__year=year,
                                                 measure_date__month=month,
                                                 measure_date__day=day,
                                                 )
                else:
                    self.title = f'{year}/{month}'
                    logger.debug(f'{self.title}')
                    return BME280.objects.filter(measure_date__year=year,
                                                 measure_date__month=month,
                                                 )
            else:
                self.title = f'{year}'
                logger.debug(f'{self.title}')
                return BME280.objects.filter(measure_date__year=year)
        logger.debug(f'{self.title}')
        return BME280.objects.all()
