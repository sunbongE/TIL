# Model 입력 메뉴얼(Article)

![image-20221020151435912](Model_Article%EB%A9%94%EB%89%B4%EC%96%BC.assets/image-20221020151435912-16662464770074.png)

처음 화면

---

- 모델 이름 : Article

  모델 필드

  | 필드 이름 | 역할      | 필드       | 속성                     |
  | --------- | --------- | ---------- | ------------------------ |
  | user      | 글 작성자 | ForeignKey | on_delete=models.CASCADE |
  | title     | 글 제목   | Char       | max_length=80            |
  | content   | 글 내용   | Text       |                          |
  | image     | 글 이미지 | Image      | upload_to=”articles/”    |
  | thumbnail | 썸네일    |            |                          |

- 모델 이름 : Comment

  모델 필드

  | 필드 이름 | 역할        | 필드       | 속성                     |
  | --------- | ----------- | ---------- | ------------------------ |
  | user      | 댓글 작성자 | ForeignKey | on_delete=models.CASCADE |
  | article   | 게시글      | ForeignKey | on_delete=models.CASCADE |
  | content   | 댓글 내용   | Char       | max_length=80            |

```python
from django.conf import settings     # settings에 저장해둔 user을 가르킴 
from django.db import models		 # db에 있는 모델 불러오기
from imagekit.models import ProcessedImageField # 썸네일에 필요함
from imagekit.processors import ResizeToFill    # 썸네일에 필요함

# Create your models here.

class Article(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #on_delete=models.CASCADE 부모객체가 삭제되면 같이 삭제됨
    title = models.CharField(max_length=10) # 제목에 최대길이 제한
    content = models.TextField()
    image = models.ImageField(upload_to="images/", blank=True) 
    #images폴더에 이미지 자동저장
    thumbnail = ProcessedImageField(
        upload_to = 'img',
        processors = [ResizeToFill(200,300)], # 썸네일 이미지 크기를 조절가능
        format = 'JPEG', # 이미지 형식 지정
        options = {'quality':60},
        blank = True) # 빈값 허용

class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    #settings.AUTH_USER_MODEL에서 설정한 User을 참조함
    article = models.ForeignKey(Article,on_delete=models.CASCADE)
    # Article모델을 참조한다는 뜻
    content = models.CharField(max_length=80)
```

**settings.AUTH_USER_MODEL**: settings.py에서 미리 설정해둔 user 정보

![image-20221020151252927](Model_Article%EB%A9%94%EB%89%B4%EC%96%BC.assets/image-20221020151252927.png)