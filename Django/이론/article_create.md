# article_create

1. url

   1. ```py
      path("create/",views.create, name="create"),
      ```

view

```py
def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False) # 저장 멈추고
            article.user = request.user 
            #article에 user(FK)값 정보를 따로 처리해야한다.
            article.save()
            return redirect('articles:index')
    else:
        article_form=ArticleForm()
    context = {
        'article_form':article_form
    }
    return render(request,'articles/create.html',context)
```

