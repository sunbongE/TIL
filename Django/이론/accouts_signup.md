# accouts_signup

1. url.py 설정

   1. ```python
      path('signup',views.signup, name='signup'),
      ```

2. views.py

   1. ```python
      def signup(request):
          if request.method == 'POST': #요청이 POST으로 오면/ 회원가입 시 처리
              accounts_form = CustomUserCreationForm(request.POST)
              if accounts_form.is_valid():
                  user = accounts_form.save() # 회원가입한 정보를 담아서
                  auth_login(request, user) # 로그인 시켜주는거
                  return redirect('account:index')
          else: # 회원가입 페이지 들어온거 처리
              accounts_form = CustomUserCreationForm()
          context = {
              'accounts_form':accounts_form, 
          }
          return render(request,'accounts/signup.html',context)
      ```

3. signup.html생성

   1. ```python
      {% extends 'base.html' %}
      {% load django_bootstrap5 %}
      {% block content %}
        <h1>
          회원 가입
        </h1>
        <form action="" method='POST'>
          {% csrf_token %} # POST요청하면 이거 써야함
          {% bootstrap_form accounts_form %} # accounts_form == view에서 넘긴거
          <input class='btn btn-success float-end' type="submit" value='가입하기'>
        </form>
      {% endblock content %}
      ```

   2. 

4. 👍끝