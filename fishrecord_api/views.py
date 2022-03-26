from django.shortcuts import render
from django.db import IntegrityError
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import *
from .serializers import *


# Create your views here.
class CreateRecord(APIView):
    def post(self, request):
        #Request data from form data
        name = request.data.get('name')
        species = request.data.get('species')
        weight = request.data.get('weight')
        length = request.data.get('length')
        longitude = request.data.get('longitude')
        latitude = request.data.get('latitude')
        image = request.data.get('image')

        #Create record object
        try:
            Record.objects.create(
                name=name, 
                species=species, 
                weight=weight,
                length=length, 
                longitude=longitude,
                latitude=latitude,
                image=image,
                )
        # In case some attributes are not provided, show error message
        except (IntegrityError, ValueError) as e:
            return Response(
                {
                    'status':'Error',
                    'detail': str(e)
                }
            )
        
        #Return response on record creation
        return Response(
            {
                'status':'Success',
                'detail':'Record Created'
            }, status = 201
        )

class GetRecord(APIView):
    def get(self, request):
        #Query all Records
        records_obj = Record.objects.all()
        #Create a serializer object based on all records obtained
        serializer_obj = RecordSerializer(records_obj, many=True)
        #Return a response consisting of all the records
        return Response(
            {
                'status':'Success',
                'Records':serializer_obj.data
            }, status=200
        )
