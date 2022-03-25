from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *

# Create your views here.
class CreateRecord(APIView):
    def post(self, request):
        name = request.data.get('name')
        species = request.data.get('species')
        weight = request.data.get('weight')
        length = request.data.get('length')
        longitude = request.data.get('longitude')
        latitude = request.data.get('latitude')
        image = request.data.get('image')

        Record.objects.create(
            name=name, 
            species=species, 
            weight=weight,
            length=length, 
            longitude=longitude,
            latitude=latitude,
            image=image,
            )
        return Response(
            {
                'status':'Success',
                'detail':'Record Created'
            }, status = 200
        )

class GetRecord(APIView):
    def get(self, request):
        records_obj = Record.objects.all()
        serializer_obj = RecordSerializer(records_obj, many=True)
        return Response(
            {
                'status':'Success',
                'Records':serializer_obj.data
            }, status=200
        )