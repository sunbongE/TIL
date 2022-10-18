from django.shortcuts import redirect, render
from .models import Article, Comment
from articles.forms import ArticleForm, CommentForm

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
            article_form.save()
            return redirect('articles:index')
    else:
        article_form = ArticleForm()
    
    context={
        'article_form':article_form
    }
    return render(request, 'articles/create.html',context)

def detail(request,pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm()
    context={
        'article':article,
        'comments': article.comment_set.all(),
        'comment_form':comment_form,
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, instance=article)
        if article_form.is_valid():
            article_form.save()
            return redirect('articles:detail', article.pk )
    else:
        article_form = ArticleForm(instance = article)

    context = {
        'article_form' : article_form,
        'article' : article,
    }
    return render(request, "articles/update.html", context)
def delete(request,pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def comment_create(request,pk)  :
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment=comment_form.save(commit=False)
        comment.article = article
        comment.save()
    return redirect('articles:detail', article.pk)

def comment_delete(request,pk,comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    comment.delete()
    return redirect('articles:detail',pk)