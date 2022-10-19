from django.conf import settings
from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail
from imagekit.processors import ResizeToFill

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='images/', blank=True)
    thumbnail = ProcessedImageField(
        upload_to = 'img',
        processors = [ResizeToFill(200,300)],
        format = 'JPEG',
        options = {'quality':60},
        blank = True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    labels = { 
            'title':'제목',
            'content':'내용',
            'updated_at':'업데이트시간',
            'image':'이미지',
            'thumbnail':'썸네일'}

class Comment(models.Model):
    content = models.CharField(max_length=80)
    article = models.ForeignKey(
        Article,
        on_delete = models.CASCADE
    )
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
