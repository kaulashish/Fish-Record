from django.db import models

# Create your models here.

class Record(models.Model):
    name = models.CharField(max_length=255)
    species = models.CharField(max_length=255)
    weight = models.FloatField()
    length = models.FloatField()
    longitude = models.FloatField()
    latitude = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, default=None)

    def __str__(self):
        return self.name