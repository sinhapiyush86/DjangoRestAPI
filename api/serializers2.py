from rest_framework import serializers
from.models import Temperature
import datetime

class TemperatureSerializer2(serializers.Serializer):
    tempdata = serializers.IntegerField()
    date = serializers.CharField()
    time = serializers.CharField()
    location = serializers.CharField()

