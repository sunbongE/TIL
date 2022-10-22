from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm, CustomUserChangeForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import get_user_model, update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm

# Create your views here.
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form':form
    }
    return render(request,'accounts/login.html',context)

def logout(request):
    auth_logout(request)
    return redirect('accounts:index')


@login_required
def index(request):
    users = get_user_model().objects.all()
    context={
        'users':users
    }

    return render(request,'accounts/index.html',context)
def signup(request):
    if request.method == 'POST': #요청이 POST으로 오면/ 회원가입 시 처리
        accounts_form = CustomUserCreationForm(request.POST)
        if accounts_form.is_valid():
            user = accounts_form.save() # 회원가입한 정보를 담아서
            auth_login(request, user) # 로그인 시켜주는거
            return redirect('accounts:index')
    else: # 회원가입 페이지 들어온거 처리
        accounts_form = CustomUserCreationForm()
    context = {
        'accounts_form':accounts_form, 
    }
    return render(request,'accounts/signup.html',context)

def delete(request):
    request.user.delete()
    auth_logout(request)
    return redirect('accounts:index')

@login_required
def detail(request, pk):
    user = get_user_model().objects.get(pk=pk)
    context = {
        'user':user,
    }
    return render(request, 'accounts/detail.html', context)

@login_required
def update(request, user_pk):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:detail', request.user.pk )
    else:
        form = CustomUserChangeForm(instance=request.user)
        
    context = {
        'form': form
    }
    return render(request, 'accounts/update.html', context)

@login_required
def password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('accounts:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form
    }
    return render(request, 'accounts/password.html', context)