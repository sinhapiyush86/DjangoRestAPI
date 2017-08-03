from rest_framework import serializers
from.models import Temperature
from datetime import datetime,date
from django.http.response import HttpResponse

class TemperatureSerializer(serializers.Serializer):
    tempdata = serializers.IntegerField()
    location = serializers.CharField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.

        """
        dnwo = datetime.now()
        return Temperature.objects.create(**validated_data,time=datetime.time(dnwo),date=date.today())
    def update(self, instance, validated_data):
        dnwo = datetime.now()
        instance.tempdata = validated_data.get("tempdata",instance.tempdata)
        instance.location = validated_data.get("location",instance.location)
        instance.time = datetime.time(dnwo)
        instance.date = date.today()
        instance.save()
        return instance
