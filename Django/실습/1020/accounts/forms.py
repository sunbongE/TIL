from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model

class CustomUserCreationForm(UserCreationForm): # 회원가입시 사용
    
    class Meta:
        model = get_user_model()
        fields = ['username', 'password1', 'password2']
        labels = {'username': '아이디', 'password1': '비밀번호', 'password2': '비밀번호확인'}
        #회원 가입시 입력 목록을 명시해주는 것

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = get_user_model()
        fields = ['first_name', 'last_name', 'email']
        # User 정보 수정 시 사용되며 마찬가지 변경 목록을 지정한것