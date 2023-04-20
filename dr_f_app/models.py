from django.db import models

class Image(models.Model):
    
    head_image = models.ImageField(upload_to='dr_f_app/images/',blank=True)
    
# Create your models here.
