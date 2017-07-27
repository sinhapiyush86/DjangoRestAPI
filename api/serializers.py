from rest_framework import serializers
from.models import Temperature
from datetime import datetime,date

class TemperatureSerializer(serializers.Serializer):
    tempdata = serializers.IntegerField()
    location = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.

        """
        dnwo = datetime.now()
        return Temperature.objects.create(**validated_data,time=datetime.time(dnwo),date=date.today())