"""Test."""
import logging
from django.test import TestCase
# from django.utils import timezone
from .models import BME280
from .stor_tph import StoreTph

logger = logging.getLogger(__name__)

# Create your tests here.
class BME280ModelTests(TestCase):
    """Test BME280Model."""

    def test_save_BM280(self):
        """Save data."""
        w_bme280 = BME280(
            temperature=0.0,
            pressure=0.0,
            humidity=0.0,
        )
        w_bme280.save()
        id = w_bme280.id
        r_bme280s = BME280.objects.filter(id=id).values()
        self.assertEqual(r_bme280s[0]['temperature'], 0.0)


class StoreTphTests(TestCase):
    """Test StoreTPH."""

    def test_save_StoreTph(self):
        """Save data."""
