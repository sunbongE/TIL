from email.policy import default
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True)
    thumbnail = ProcessedImageField(
        upload_to = 'img',
        processors = [Thumbnail(200,300)],
        format = 'JPEG',
        options = {'quality':60},
        blank = True)
    