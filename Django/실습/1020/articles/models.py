from django.conf import settings
from django.db import models
from imagekit.models import ProcessedImageField # 썸네일에 필요함
from imagekit.processors import ResizeToFill    # 썸네일에 필요함

# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True)
    thumbnail = ProcessedImageField(
        upload_to = 'img',
        processors = [ResizeToFill(200,300)],
        format = 'JPEG',
        options = {'quality':60},
        blank = True)

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    content = models.CharField(max_length=80)