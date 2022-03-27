from rest_framework import serializers

from .models import *


class RecordSerializer(serializers.ModelSerializer):
    timestamp = serializers.DateTimeField(format='%d-%m-%y %H:%M')
    image = serializers.SerializerMethodField('get_image_url')
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
            'image',
        ]
    #Get absolute url of image
    def get_image_url(self, obj):
        request = self.context["request"]
        return request.build_absolute_uri(obj.image.url)