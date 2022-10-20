# Password변경

1. url.py

   1. ```py
      path('password/', views.password, name='password'),
      ```

2. views.py

   1. ```py
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
      ```

3. template

   1. ```py
      {% extends 'base.html' %}
      {% load django_bootstrap5 %}
      {% block content %}
        <h1>비밀번호 변경</h1>
        <form action="{% url 'accounts:password' %}" method="POST">
          {% csrf_token %}
          {% bootstrap_form form %}
          {% bootstrap_button button_type="submit" button_class="btn-primary" content="수정완료" %}
        </form>
      {% endblock %}
      ```

👍