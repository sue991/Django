from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill

# Create your models here.

class Blog(models.Model):
    text = models.TextField()
    image = models.ImageField(upload_to = "blogimg",null=True,default='')
    image_thumbnail = ImageSpecField(source = 'image', processors = [ResizeToFill(120,60)])