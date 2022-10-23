# django-message

message기능은 이미 장고에서 제공하는 기능이다.

그래서 별도의 설치없이 사용 가능!

### 메시지 레벨

| 레벨    | 용도                                                 |
| ------- | ---------------------------------------------------- |
| debug   | 프로덕션 배포에서 무시(또는 제거)될 개발 관련 메시지 |
| info    | 자용자를 위한 정보 메시지                            |
| success | 작업을 성공함을 알림                                 |
| warning | 장애가 발생하지 않았지만 임박했을 수 있음            |
| error   | 작업이 성공 하지 못 했거나 다른 오류가 발생했습니다. |

예시

```py
#views.py
messages.debug(request, '%s SQL statements were executed.' % count)
messages.info(request, 'Three credits remain in your account.')
messages.success(request, 'Profile details updated.')
messages.warning(request, 'Your account expires in three days.')
messages.error(request, 'Document deleted.')
```





## 설정

settings.py 에서 아래 코드 추가 

```py
MESSAGE_STORAGE = 'django.contrib.messages.storage.cookie.CookieStorage'  
```



base.html에서 아래 코드 추가

```html
{% if messages %}
    {% for message in messages %}
      <div class="alert alert-{{ message.tags }}">
        {{ message }}
      </div>
    {% endfor %}
  {% endif %}
```







## 사용 예시

views.py

로그아웃, 로그인, 회원가입, 수정 등에 작업이 성공적으로 수행되었음을 알리는 기능

```py
from django.contrib import messages

def logout(request):
    auth_logout(request)
    messages.warning(request, '로그아웃 하였습니다.') # 로그아웃 하면 알려줌
    return redirect('articles:index')
```

