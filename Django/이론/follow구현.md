# follow구현



### models.py

자기 자신을 참조해야하는 상황에서 self으로 사용한다.

```py
models.ManyToManyField('self', symmetrical=False, related_name ='followers')
```



**symmetrical=False** 

한 쪽에서 팔로우 한다고 친구가 되지 않기 때문에(대칭관계가 아니기 때문에) 

False라고 생각하면 된다. 

```py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    followings=models.ManyToManyField('self',symmetrical=False,related_name='followers')

```



### urls.py

```py
urlpatterns = [
    path('<int:pk>/follow/',views.follow,name='follow'),
]
```



### views.py

```py
def follow(request,pk):
    user = get_user_model().objects.get(pk=pk)
    if request.user == user: # 스스로 팔로우는 하는 것 방지
        messages.warning(request,'스스로는 팔로우할 수 없어요.')
        return redirect('accounts:detail',pk)
    
    if request.user in user.followers.all(): # 이미 팔로우한 유저라면
        user.followers.remove(request.user)  # 취소
    else:
        user.followers.add(request.user)  	 # 팔로우
    return redirect('accounts:detail',pk)	 
```



### template

스스로 팔로우 못하게 처리함

요청한 유저가 이미 팔로우 했다면 팔로우 취소 버튼이 나오도록 분기처리함

```django
 {% if request.user != user %}  
      {% comment %} 스스로는 팔로우 불가능 처리 {% endcomment %}
      <a href="{% url 'accounts:follow' user.pk %}" class='btn btn-primary float-end'>
        {% if request.user in user.followers.all %}
        팔로우 취소
        {% else %}
        팔로우
        {% endif %}
      </a>
      {% endif %}
      <p class='text-muted'>
        팔로우
        {{ user.followings.count}}
        | 팔로워
        {{user.followers.count}}</p>
      <hr><br>
```

