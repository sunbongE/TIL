# accounts_update

1. urls.py

   1. ```py
          path('<int:pk>/update/',views.update, name='update'),
      ```

2. views

   1. ```py
      
      def update(request,pk):
          if request.method == 'POST':
              accounts_form = CustomUserChangeForm(request.POST,instance=request.user)
              if accounts_form.is_valid():
                  accounts_form.save()
                  return redirect('accounts:detail', request.user.pk)
          else:
              accounts_form = CustomUserChangeForm(instance=request.user)
          context = {
              'accounts_form':accounts_form
          }
          return render(request,'accounts/update.html',context)
      
      ```

3. tem

   1. ```py
      {% extends 'base.html' %}
      {% load django_bootstrap5 %}
      {% block content %}
        <h1>
          수정
        </h1>
        <form action="" method='POST'>
          {% csrf_token %}
          {% bootstrap_form accounts_form %}
          <input class='btn btn-success float-end' type="submit" value='수정하기'>
        </form>
      {% endblock content %}
      ```

4. 👍