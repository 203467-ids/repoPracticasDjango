from django.db import models
from django.utils import timezone

# Create your models here.
class ImagenTabla(models.Model):
    name= models.CharField(max_length=50, null = True)
    url= models.ImageField(null=True,blank=True, default='', upload_to='assets/img/')
    format= models.CharField(max_length=50, null = True)
    