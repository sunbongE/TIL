from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm):
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']
        labels = {'username': '아이디', 'password1': '비밀번호', 'password2': '비밀번호확인'}

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']