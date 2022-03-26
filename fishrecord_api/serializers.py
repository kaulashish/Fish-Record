from rest_framework import serializers

from .models import *


class RecordSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format='%d-%m-%y %H:%M')
    class Meta:
        model = Record
        fields = [
            'name',
            'species',
            'weight',
            'length',
            'longitude',
            'latitude',
            'timestamp',
            'image'
        ]
