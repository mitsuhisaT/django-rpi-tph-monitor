"""
Serializers.

@date 16 December 2019
@author mitsuhisaT <asihustim@gmail.com>
"""
from rest_framework import serializers
from monitor.models import BME280


class BME280Serializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = BME280
        fields = ['id', 'pressure', 'humidity', 'temperature',
                  'measure_date']
