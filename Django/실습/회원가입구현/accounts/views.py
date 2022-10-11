from django.shortcuts import redirect, render
# from accounts.models import User
from django.contrib.auth import get_user_model
# from django.contrib.auth.forms import UserCreationForm
from .forms import CustomUserCreatoinForm
from .models import User
# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreatoinForm(request.POST)
        if form.is_valid():
            form.save()
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