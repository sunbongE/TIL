# ariticle_delete

urls.py

```py
path('<int:pk>/delete/',views.delete,name='delete'),
```



views.py

역시 요청으로 받은 pk와 모델에 있는 pk가 같은 것을 찾아서 삭제하는 방법이다.

```py
def delete(request,pk):  
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```

