from django.shortcuts import redirect, render
from .models import Article, Comment
from articles.forms import ArticleForm, CommentForm
from django.contrib import messages
# Create your views here.
def main(request):
    return render(request,'articles/main.html')
def index(request):
    articles = Article.objects.all()

    context={
        'articles':articles
    }
    return render(request,'articles/index.html',context)


def create(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            article = article_form.save(commit=False)
            # 로그인한 유저 => 작성자네!
            article.user = request.user 
            article.save()
            messages.success(request, '글 작성이 완료되었습니다.')
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
    if request.user == article.user:
        if request.method == 'POST':
            article_form = ArticleForm(request.POST, instance=article)
            if article_form.is_valid():
                article_form.save()
                messages.success(request, '글이 수정되었습니다.')
                return redirect('articles:detail', article.pk )
        else:
            article_form = ArticleForm(instance = article)

        context = {
            'article_form' : article_form,
            'article' : article,
        }
        return render(request, "articles/update.html", context)
    else:
        # 작성자가 아닐 때
        # (1) 403 에러메시지를 던져버린다. 
        # from django.http import HttpResponseForbidden
        # return HttpResponseForbidden()
        # (2) flash message 활용!
        messages.warning(request, '작성자만 수정할 수 있습니다.')
        return redirect('articles:detail', article.pk)

def delete(request,pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')

def comment_create(request, pk):
    article = Article.objects.get(pk=pk)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
        comment=comment_form.save(commit=False)
        comment.article = article
        comment.user = request.user
        comment.save()
    return redirect('articles:detail', article.pk)

def comment_delete(request,pk,comment_pk):
    comment = Comment.objects.get(pk = comment_pk)
    if request.user == comment.user:
        comment.delete()
    return redirect('articles:detail',pk)