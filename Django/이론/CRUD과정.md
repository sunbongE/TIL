# CRUD 과정 (게시판)

main 화면 

## 1. Read_0 (index)

1. 가상 환경
2. 활성화
3. 장고 설치
4. 프로젝트 생성
5. 앱 생성 및 등록(settings.py)
6. index 작성
   1. 글 작성 버튼을 만들어 new의 url에 요청을 한다.
7. new페이지 (글 작성)
   1. 제목과 내용을 POST으로 요청한다
   2. {% csrf_token %} 이 코드를 붙어야 한다. (보안 때문)
8. views.py에서 request.POST.get() 으로 바꿔야함



CRUD

## create

1. new에서 url 요청
2. views 입력

```python
def create(request):
    title = request.POST.get('title')
    content = request.POST.get('content')
    Article.objects.create(title=title, content=content)

    return redirect('articles:index')
```

ModelForm 사용

1. 앱 폴더에 forms.py파일은 만들고 장고의 forms기능과 모델을 불러온다.

```python
# forms.py
from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
	# 정보를 작성
    class Meta:
        model = Article
        fields = ['title','content'] #field의 정보를 폼에 적용함

```

views.py에서 new와create 의 코드는 매우 비슷하여 하나로 합쳐 쓸 수 있는데

요청이 GET으로 들어올 때와 POST 으로 들어오는 경우를 나누어서 사용할 수 있다.

```python
#views.py
def create(request):
    if request.method == 'POST': # 요청이 POST으로 들어오면
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:index')
    else: # 요청이 GET으로 
        article_form = ArticleForm()
    context = {  # 이 코드는 밖에 있어야 두가지 경우 모두 응답을 받을 수 있어서 밖에있음
        'article_form':article_form
    }

    return render(request,'articles/new.html', context)
```

이런 방법을 사용하려면

1. index,html에서 보내주던 요청도 new -> create으로 변경
2. urls.py의 new는 없어도 되니까 삭제
3. views.py에 ArticleForm을 불러와야 함



## Read_1 (detail)

1. index.html에서 제목을 누르면 내용을 볼 수 있는 기능
2. title에 a태그로 detail url을 요청
3.  url은 동적인 인자를 받을 수 있게 만들어 줘야 선택한 데이터를 알 수 있다.

```python
#views.py
def detail(request, pk):
    
    article = Article.objects.get(pk=pk) # 클릭한 제목에 해당하는 pk를 가져와 구분

    context = {	# 정보를 넘겨 줘야 하기때문에 작성함
        'article':article
    }

    return render(request, 'articles/detail.html', context)
```



```django
<!--detail.html -->
{% extends 'base.html' %}
{% block content %}
<h1>{{ article.pk }}번째 글</h1>
<p>title : {{ article.title }}</p>
<p>content : {{ article.content }}</p>
<a href="{% url 'articles:index' %}">home</a>
{% endblock %}
```



## update

업데이트는 처음 들어올 때 와 수정한 값을 보낼 때로 나누어서 views.py를 작성했음

(GET,POST)

1. detail.html에서 수정하기 버튼을 만들어서 주소 요청하고 pk값도 보낸다.

2.  `path('<int:pk>/update/', views.update, name='update')` url

   

```python

def update(request, pk):
    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        article_form=ArticleForm(request.POST, instance=article) #수정 값 가져옴
        # instance=article 이거는 전에 작성한 내용을 그대로 가져오기위함
        if article_form.is_valid(): # 유효성검사에 통과하면 저장
            article_form.save()
            return redirect('articles:detail',article.pk)#디테일화면으로
    else:
        article_form = ArticleForm(instance=article)
    context={
        'article_form': article_form
    }
    return render(request,'articles/update.html',context)
```





## Delete

아주 간단함/ 받아온 pk 값의 데이터를 지우는 코드를 작성

```python
    
def delete(request,pk):
    article = Article.objects.get(pk=pk) #프라이머리키로 어떤 데이터인지 구분

    article.delete() # 삭제
    return redirect('articles:index')
```







-----

### base.html 사용법

![image-20221005142637055](CRUD%EA%B3%BC%EC%A0%95.assets/image-20221005142637055.png)

파일을 바탕이 되는 위치 최 상위에 만들어 준다.

{% block content %}

​    {% endblock %}

위 코드를 제외한 모든 코드가 그대로 복사되어 가져오는 개념이라고 생각하면 된다.

코드 사이에는 그 페이지에 맞는 내용을 채워 넣으면 된다.

### 적용 방법

```django
{% extends 'base.html'%} <!-- 처음 시작 -->

{% block content %}
<h1>게시판</h1>
<!-- 이곳에 내용을 채움 -->
{% endblock %}
```

