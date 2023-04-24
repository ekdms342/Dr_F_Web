from django.db import models

class Image(models.Model):
    
    image = models.ImageField(upload_to='dr_f_app/images/',blank=True)
    csv = models.FileField(upload_to='dr_f_app/csv/',blank=True)
    
# Create your models here.
