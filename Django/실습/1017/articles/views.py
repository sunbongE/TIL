from django.shortcuts import redirect, render
from articles.forms import ArticleForm
from django.contrib import messages
from articles.models import Article

# Create your views here.

def index(request):
    articles = Article.objects.all()
    context = {
        'articles':articles
    }
    return render(request,'articles/index.html',context)

def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, '글 작성되었습니다.')
            return redirect('articles:index')
    else:
        form = ArticleForm()
    
    context = {
        'form':form
    }



    return render(request, 'articles/create.html',context)

def detail(request,pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article':article
    }
    return render(request,'articles/detail.html',context)

def delete(request,pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    messages.warning(request,'삭제했슴다.')
    return redirect('articles:index')

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        form = ArticleForm(request.POST,request.FILES,instance=article)
        if form.is_valid():
            form.save()
            messages.success(request,'수정했습니다!')
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=article)
    
    context = {
        'article':article,
        'form':form,
    }
    return render(request, "articles/update.html", context)
