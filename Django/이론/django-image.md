# django-image 사용법

적용 순서 (모델은 이미 만들어진 것으로 가정)

1. 파일 설치
2. settings.py에 추가 및 설정
3. pjt/urls.py 설정
4. html에서 POST요청 인코딩 속성 적용
5. views.py에 create, update에 request.FILES 적용
6. 이미지 출력! 👍

## imagekit

설치 파일

```bash
$ pip install pillow # django-imagekit 사용을 위해서 사전 설치 필요
$ pip install pilkit # django-imagekit 사용을 위해서 사전 설치 필요
$ pip install django-imagekit

# pip 설치 후, settings.INSTALLED_APPS에 imagekit 추가 필요
```



1. **Pillow** : Pillow는 PIL 프로젝트에서 fork 되어서 나온 라이브러리로, PIL이 python 3를 지원하지 않기 때문에 pillow를 많이 사용하는 추세 (ImageField 사용시 필수)

2. **django-imagekit** : 이미지 썸네일 helper 장고 앱 (실제 이미지 처리시에는 PILKit 이 사용됨)
3. 설치 후 settings.INSTALLED_APPS에 imagekit추가 필요



### 사용 예시

모델 마이그레이션 / 마이크레이트 

```py
# models.py
from django.db import models     # db에서 모델
from imagekit.models import ProcessedImageField #원본 이미지를 재가공하여 저장할 수 있게 도움
from imagekit.processors import Thumbnail # 썸네일

# Create your models here.

class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    image = models.ImageField(upload_to='images/', blank=True) # 원본 이미지
    thumbnail = ProcessedImageField(			 # 썸네일 이미지
        upload_to = 'img', 						 # 이미지 저장
        processors = [Thumbnail(200,300)],		 # 크기 조절
        format = 'JPEG',						 # 최종 저장 포맷
        options = {'quality':60},				 # 저장 옵션
        blank = True)							 # 빈값 허용
    
```



settings.py

```py
INSTALLED_APPS = [
    'articles',
    'imagekit', # 설치 파일 설치 후 적용
]

STATIC_URL = '/static/'  
# 개발자가 관리하는 파일

MEDIA_ROOT = BASE_DIR / 'images' 
# 사용자가 업로드한 파일이 저장된다.

MEDIA_URL = '/media/'
```





Project / urls.py 

**+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)** - 추가

```py
# pjt/urls.py 
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('articles.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)# 이거 추가

    
```



articles/views.py

폼을 받을 때 **request.FILES** 으로 넘겨줘야 이미지를 받을 수 있다. 

```py
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES) # 이미지 파일을 받기 위함
        if form.is_valid():
            form.save()
            messages.success(request, '글 작성되었습니다.')
            return redirect('articles:index')
    else:
        form = ArticleForm()
    
    context = {
        'form':form
    }

```





### enctype

> 인코딩이란?
>
> 파일에 저장된 정보의 형태를 다른 것으로 변경하는 것을 말한다. 
>
> 부호화 라고도 한다.

HTML폼을 POST방식으로 전송할 때는 전송하는 데이터를 인코딩하기 위해 인코딩 타입에 대한 명시가 필요하다.

인코딩 타입을 명시하는 속성은 **enctype** 이다. 

enctype 은 3가지 속성을 가지고 있고 정리하자면 아래와 같음

| enctype                            | 용도                                                         |
| ---------------------------------- | ------------------------------------------------------------ |
| multipart/form-data                | 파일(\<input type="file">)이 포함된 폼을 전송할 때 사용.     |
| application/x-www-form-urlcencoded | 파일이 없는 폼에 사용. multipart/form-data 를 제외한 모든 경우에 사용. enctype 속성이 없을 때 적용 기본 값. |
| text/plain                         | 인코딩 없이 전송. 보안성이 없어 디버깅 용도로만 사용해야 함. |

우리가 사용할 속성은 **multipart/form-data **이다.

적용 법

articles / create.html

form에 속성 추가

```py
# create.html
{% extends 'base.html' %}
{% load django_bootstrap5 %}
{% block content %}
  <div class="container">
    <form class='text-warning' action="{% url 'articles:create' %}" method="POST" enctype="multipart/form-data"> # 여기 이 부분!!!!

      {% csrf_token %}
      {% bootstrap_form form %}
      <div class='d-flex justify-content-end'>

        <input class="btn btn-outline-success mx-3" type="submit" value='Submit'>
        <a class="btn btn-outline-primary" href="{% url 'articles:index' %}">Home</a>
      </div>
    </form>
  </div>
{% endblock content %}

```



이미치 출력!

```py
<img src"{{ article.image.url }}"> 
#해당 글의 db에 저장된 image에 접근해서 출력 가능
```

