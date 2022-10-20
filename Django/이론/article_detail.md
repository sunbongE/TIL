# article_detail



url.py

```py
path('<int:pk>',views.detail, name='detail'),
```





views.py

받은 pk와 모델에 있는 pk가 같은 경우를 찾아서 detail 페이지를 찾아가는 것

```py
def detail(request, pk):
    article = Article.objects.get(pk=pk) #받은 pk와 모델에 있는 pk가 같은 경우
    context={
        'article':article
    }
    return render(request,'articles/detail.html',context)
    
```





detail.html

```py
{% extends 'base.html' %}

{% block content %}
  <h1>
    {{ article.user }}님 # 글쓴이
  </h1>
  <p>{{ article.title }}</p>
  <p>{{ article.content }}</p>
{% endblock content %}
```

