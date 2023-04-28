from django.db import models

class Image(models.Model):
    
    image = models.ImageField(upload_to='images/',blank=True)
    csv = models.FileField(upload_to='csv/',blank=True)
    
# Create your models here.
