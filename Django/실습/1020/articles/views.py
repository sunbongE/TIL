from multiprocessing import context
from django.shortcuts import redirect, render

from articles.forms import ArticleForm, CommentForm
from articles.models import Article

# Create your views here.
def index(request):
    articles = Article.objects.all()
    context={
        'articles':articles
    }
    return render(request,'articles/index.html',context)

def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            article.user = request.user
            article.save()
            return redirect('articles:index')
    else:
        article_form=ArticleForm()
    context = {
        'article_form':article_form
    }
    return render(request,'articles/create.html',context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context={
        'article':article,
        'comment_form':comment_form,
    }
    return render(request,'articles/detail.html',context)

def delete(request,pk): 
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

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

def comment_create(request,pk):
    article =Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()  
   
    return redirect('articles:detail', article.pk)

