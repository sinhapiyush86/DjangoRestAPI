from rest_framework import serializers
from.models import Temperature

class TemperatureSerializer(serializers.Serializer):
    tempdata = serializers.IntegerField()

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Temperature.objects.create(**validated_data)