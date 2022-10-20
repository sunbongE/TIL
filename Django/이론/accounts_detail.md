# accounts_detail

1. urls.py

   1. ```python
          path('<int:pk>/',views.detail, name='detail'),
      ```

2. views.py

   1. ```py
      def detail(request, pk):
          user = get_user_model().objects.get(pk=pk)
          context = {
              'user':user,
          }
          return render(request, 'accounts/detail.html', context)
      ```

3. template

   1. ```py
      {% extends 'base.html' %}
      
      {% block content %}
        <h1>
          {{user.username}}님 프로필
        </h1>
      
      {% endblock content %}
      ```

