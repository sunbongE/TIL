# articles_like_button

models.py

`like_users=models.ManyToManyField(settings.AUTH_USER_MODEL,related_name='like_articles')`

```py
class Article(models.Model):
    title = models.CharField(max_length=80)
    content = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_articles') # 이 부분
     
```

related_name(역참조 이름)을 설정하지 않으면 에러 메시지가 뜨는데 그 이유는 artciel.user(글쓴사람)을 역참조할 때 이름이 겹치기 때문이다. 그래서 별도로 역참조할 때 사용할 이름을 정해준다.

사용 예시

```py
article.like_articles.add()
```

`makemigrations`,` migrate` 진행 



urls.py

```
path('<int:article_pk>/like/',views.like, name='like'),
```



views.py

```py
@login_required
def likes(request,article_pk):
    article = Article.objects.get(pk=article_pk)
    # if request.user in article.like_users.all(): # 데이터베이스를 전부 들고와서 비교
    if article.like_users.filter(pk=request.user.pk).exists(): 
    # request.user가 있는지만 확인하는 것 속도생각하면 이 방법이 더 좋은거
        article.like_users.remove(request.user) #사용자 제거
    else:
        article.like_users.add(request.user) # 사용자 추가
    return redirect('articles:detail',article_pk)
```



template

```django
{% comment %} 좋아요 개수 출력 {% endcomment %}
{{ article.like_users.count }}개
{% comment %} 좋아요를 눌렀는지 분기처리 {% endcomment %}
{% if request.user in article.like_users.all %}
{% comment %} article의 like테이블에 사용자가 좋아요를 눌렀는지 확인하여 
좋아요 취소 구현할 때 사용  {% endcomment %}

```

