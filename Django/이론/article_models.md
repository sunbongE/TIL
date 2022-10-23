# article_models

```py
from django import forms
from .models import Article, Comment  #  모델 불러옴

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title','content','image','thumbnail'] # 필드 지정
        labels = { 						# 라벨 지정으로 화면에 보이는 글 변경 가능
            'title':'제목',
            'content':'내용',
            'image':'원본이미지',
            'thumbnail':'썸네일',

        }

        
class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ["content",]
        # __all__으로 하면 사용자를 글쓴이가 정할 수 있는 이상한 일이 벌어지기 때문에 
        # 직접 필드를 설정합니다!
```

