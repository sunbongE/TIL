# accounts_login_logout



## login

`AuthenticationForm`: 유저가 존재하는지를 검증하는 장고 내장 모델 폼.

사용자가 로그인 폼에 작성한 정보가 유효한지 검증해줌

1. url,py

   1. ```py
      path('login/',views.login, name='login'),
      ```

2. views.py

   1. ```python
      def login(request):
          if request.method == 'POST':
              form = AuthenticationForm(request, data=request.POST)
              if form.is_valid():
                  auth_login(request, form.get_user())
                  return redirect('accounts:index')
      
          else:
              form = AuthenticationForm()
          context = {
              'form':form
          }
          return render(request,'accounts/login.html',context)
      ```

3. template

```py
{% extends 'base.html' %}
{% load django_bootstrap5 %}
{% block content %}
  <h1>로그인</h1>

  <form action="" method="POST">
    {% csrf_token %}
    {% bootstrap_form form %}
    {% bootstrap_button button_type="submit" button_class="btn-primary" content="로그인" %}
  </form>
{% endblock %}

```

## logout

url

```py
    path('logout/',views.logout, name='logout'),
```

view

```py
@login_required # 로그인 됐을 때만 
def logout(request):
    auth_logout(request)
    messages.warning(request, '로그아웃 하였습니다.') # 
    return redirect('accounts:index')

```

👍