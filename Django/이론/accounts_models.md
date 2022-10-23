# accounts_models

```py
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    
    @property
    def full_name(self): # 필수 아님 / 기본 : pass
        return f'{self.last_name}{self.first_name}'

```

