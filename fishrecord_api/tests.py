import io

import numpy as np
from django.urls import reverse
from PIL import Image
from rest_framework import status
from rest_framework.test import APITestCase

# Create your tests here.

class CreateRecordTestCase(APITestCase):
    def generate_photo_file(self):
        file = io.BytesIO()
        #Create a random image of size 500px x 500px
        arr = np.random.randint(0,255,(500,500,3))
        image = Image.fromarray(arr,'RGB')
        #save file as png
        image.save(file, 'png')
        file.name = 'test.png'
        file.seek(0)
        return file

    def test_create_record(self):
        file = self.generate_photo_file()
        #Provide sample data 
        sample_data = {
            'name':'test',
            'species':'species',
            'length':10,
            'weight':2.2,
            'longitude':122.2,
            'latitude':80.2,
            'image':file
        }
        #return response
        response = self.client.post(reverse('create'), sample_data)
        #check response status
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
