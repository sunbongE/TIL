# article_update

urls.py

```py
path('<int:pk>/update/',views.update,name='update'),
```

views.py

수정하는 기능이기 때문에 입력란이 비어있으면 안된다.

비어있으면 create와 다를게 없기 때문에 instance= article으로 정보를 채워주고

수정한 후 리턴은 해당 detail 페이지로 가야하니까 article.pk를 넘겨줘야 해당 글을 찾을 수 있다..



```py
def update(request,pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save() 
            return redirect('articles:detail', article.pk )
    else:
        form = ArticleForm(instance=article)
    context = {
        'form':form
    }
    return render(request,'articles/update.html',context)
```



update.html

```py
{% extends 'base.html' %}
{% load django_bootstrap5 %}
{% block content %}
  <h1>
    글 수정
  </h1>
  <form action="" method='POST'>
    {% csrf_token %}
    {% bootstrap_form form %}
    <input class='btn btn-success float-end' type="submit" value='작성'>
  </form>
{% endblock content %}
```

❌ <a class='btn btn-success float-end' href="{% url 'update' %}" type="submit" value='작성'>

❗복 붙을 하다가 깜빡하고 a테그로 버튼 후 href으로 경로를 정하는데 이러면 POST요청이 아닌 GET으로

❗요청되어 같은 화면에서 맴돌게 되니까 주의하자❗