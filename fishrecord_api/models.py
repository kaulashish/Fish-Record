from django.db import models
from PIL import Image

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

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.name

    #override save method to resize image to 140px x 140px
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        image = Image.open(self.image)
        #Resize image if image height and width is greater than 140px
        if image.height > 140 and image.width > 140:
            output_size = (140, 140)
            image = image.resize(output_size, Image.ANTIALIAS)
            image.save(self.image.path)
