from django.contrib import admin
from django.contrib.auth.forms import UserCreationForm
# from .models import User
from django.contrib.auth import get_user_model

class CustomUserCreatoinForm(UserCreationForm):

    class Meta:
        model = get_user_model()
        fields = ('username', )
