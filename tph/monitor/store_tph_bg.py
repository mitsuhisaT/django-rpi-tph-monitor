"""Background store temperature, pressure and humidity from BME230I2C."""
from background_task import background
from datetime import timedelta
from django.utils import timezone
import logging
from .store_tph import StoreTph
import tph.settings as ts


logger = logging.getLogger(__name__)


@background
def bgStoreTph():
    """
    Background store TPH.

    Params:
        schedule: timedelta
            schedule=90  # 90 seconds from now
            schedule=timedelta(minutes=20)  # 20 minutes from now
            schedule=timezone.now()  # at a specific time
        repeat: time offset (seconds)
            repeat=Task.NEVER (deffault)
            repeat=Task.HOURLY (or DAILY, WEEKLY, EVERY_2_WEEKS, EVERY_4_WEEKS)
        repeat_until: datetime or None

    See: https://django-background-tasks.readthedocs.io/en/latest/

    """
    logger.debug('start')
    storeTph = StoreTph(ts.BME280CH1_ADDR)
    id = storeTph.save()
    logger.debug(f'end, store id: {id}')
