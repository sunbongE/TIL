from django.shortcuts import redirect, render

from django.contrib.auth.forms import AuthenticationForm

from django.contrib.auth import get_user_model
from traitlets import Instance
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreatoinForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreatoinForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user) # 회원가입 시 로그인 됨
            return redirect('movies:index')
    else:

        form = CustomUserCreatoinForm()

    context = {
        'form':form
    }

    return render(request, 'accounts/signup.html',context)

def detail(request, pk):
    
    user = get_user_model().objects.get(pk=pk)
    
    context = {
        'user':user
    }

    return render(request, 'accounts/detail.html',context)

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('movies:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }

    return render(request, 'accounts/login.html', context)

def logout(request):
    auth_logout(request)
    return redirect('movies:index')

@login_required
def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail',request.user.pk)
    else:
        form = CustomUserChangeForm(instance=request.user) 
    
    context = {
        'form':form
    }
    return render(request,'accounts/update.html',context)

def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('movies:index')