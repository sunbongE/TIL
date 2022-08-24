from django.db import models

# 장르 클래스를 만드는데 models.Model 내부 클래스를 상속받음
# 미리 만들어진 기능들을 활용하기 위해서
class Genre(models.Model):
    name = models.CharField(max_length = 30)
