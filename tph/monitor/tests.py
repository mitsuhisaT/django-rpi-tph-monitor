"""Test."""
from datetime import date, datetime, timedelta
import logging
import time
from django.conf import settings as ts
from django.utils import timezone
from django.test import TestCase
from django.utils import timezone
from monitor.data_container import BME280dc
from monitor.models import BME280
from monitor.store_tph import StoreTph

# logger = logging.getLogger(__name__)


class BME280ModelTests(TestCase):
    """Test BME280Model."""

    def test_save_BME280(self):
        """Save data."""
        w_bme280 = BME280(
            temperature=0.0,
            pressure=0.0,
            humidity=0.0,
        )
        w_bme280.save()
        id = w_bme280.id
        r_bme280 = BME280.objects.get(id=id)
        self.assertEqual(r_bme280.temperature, 0.0)

    def test_get_lastmonth_BME280(self):
        """Get last month data."""
        tMonth = timezone.now().replace(day=1)
        lMonth = tMonth - timedelta(days=1)
        tYear = tMonth.year
        lYear = tYear - 1

        w_bme280 = BME280(
            temperature=15.0,
            pressure=0.0,
            humidity=0.0,
        )
        w_bme280.save()
        w_bme280.measure_date = datetime(lYear, tMonth.month, 15, 12, 34, 56)
        w_bme280.save()

        w_bme280 = BME280(
            temperature=15.0,
            pressure=0.0,
            humidity=0.0,
        )
        w_bme280.save()
        w_bme280.measure_date = datetime(tYear, tMonth.month, 15, 12, 34, 56)
        w_bme280.save()

        w_bme280 = BME280(
            temperature=15.0,
            pressure=0.0,
            humidity=0.0,
        )
        w_bme280.save()

        w_bme280 = BME280(
            temperature=14.9,
            pressure=0.0,
            humidity=0.0,
        )
        w_bme280.save()
        w_bme280.measure_date = datetime(tYear, lMonth.month, 15, 12, 34, 56)
        w_bme280.save()
        # time.sleep(5)

        # https://docs.djangoproject.com/en/3.0/ref/databases/#sqlite-notes
        bme280s = BME280.objects.filter(measure_date__month=lMonth.month)
        self.assertEqual(bme280s[0].temperature, 14.9)

class BME280dcTests(TestCase):
    """Teest data container BME280dc."""

    def test_get_BME280dc_t(self):
        """Get datas."""
        temperature = 17.6
        pressure = 1025
        humidity = 52
        w_bme280dc = BME280dc(t=temperature, p=pressure, h=humidity)
        self.assertEqual(temperature, w_bme280dc.t)

    def test_get_BME280dc_p(self):
        """Get datas."""
        temperature = 17.6
        pressure = 1025
        humidity = 52
        w_bme280dc = BME280dc(t=temperature, p=pressure, h=humidity)
        self.assertEqual(pressure, w_bme280dc.p)

    def test_get_BME280dc_h(self):
        """Get datas."""
        temperature = 17.6
        pressure = 1025
        humidity = 52
        w_bme280dc = BME280dc(t=temperature, p=pressure, h=humidity)
        self.assertEqual(humidity, w_bme280dc.h)

    def test_get_BME280dc_mdt(self):
        """Get datas."""
        temperature = 17.6
        pressure = 1025
        humidity = 52
        w_bme280dc = BME280dc(t=temperature, p=pressure, h=humidity)
        self.assertIsInstance(w_bme280dc.mdt, datetime)

    def test_set_BME280dc_t(self):
        """Set datas."""
        temperature = 17.6
        pressure = 1025
        humidity = 52
        w_bme280dc = BME280dc(t=temperature, p=pressure, h=humidity)
        w_bme280dc.t = 5.8
        self.assertEqual(5.8, w_bme280dc.t)

    def test_set_BME280dc_p(self):
        """Set datas."""
        temperature = 17.6
        pressure = 1025
        humidity = 52
        w_bme280dc = BME280dc(t=temperature, p=pressure, h=humidity)
        w_bme280dc.p = 987
        self.assertEqual(987, w_bme280dc.p)

    def test_set_BME280dc_h(self):
        """Set datas."""
        temperature = 17.6
        pressure = 1025
        humidity = 52
        w_bme280dc = BME280dc(t=temperature, p=pressure, h=humidity)
        w_bme280dc.h = 24
        self.assertEqual(24, w_bme280dc.h)


class StoreTphTests(TestCase):
    """Test StoreTPH."""

    def test_save_StoreTph(self):
        """Save data."""
        storeTph = StoreTph(ts.BME280CH1_ADDR)
        id = storeTph.save()
        mbe280 = BME280.objects.filter(id=id).get()
        self.assertEqual(id, mbe280.id)

    def test_betweenDatetime(self):
        """Get data."""
        startdt = timezone.now()
        for i in range(5):
            storeTph = StoreTph(ts.BME280CH1_ADDR)
            storeTph.save()
            time.sleep(1)
        bdt = startdt + timedelta(seconds=1)
        edt = startdt + timedelta(seconds=4)
        bme280s = storeTph.betweenDatetime(bdt=bdt, edt=edt)
        self.assertEqual(len(bme280s), 3)
