from django.db import models

# 장르 클래스를 만드는데 models.Model 내부 클래스를 상속받음
# 미리 만들어진 기능들을 활용하기 위해서


class Director(models.Model):
    name = models.TextField(null=True,default='')
    debut = models.DateTimeField(null=True,default='')
    country = models.TextField(null=True,default='')

class Genre(models.Model):
    title = models.TextField(null=True,default='')

# 3 테이블에 데이터 추가
Director.objects.create(name='봉준호',debut='1993-1-1',country='KOR')
Director.objects.create(name='김한민',debut='1999-1-1',country='KOR')
Director.objects.create(name='최동훈',debut='2004-1-1',country='KOR')
Director.objects.create(name='이정재',debut='2022-1-1',country='KOR')
Director.objects.create(name='이경규',debut='1992-1-1',country='KOR')
Director.objects.create(name='한재림',debut='2005-1-1',country='KOR')
Director.objects.create(name='Joseph Kosinski',debut='1999-1-1',country='KOR')
Director.objects.create(name='김철수',debut='2022-1-1',country='KOR')

# 4 genre에 추가
Genre.objects.create(title = '액션')
Genre.objects.create(title = '드라마')
Genre.objects.create(title = '사극')
Genre.objects.create(title = '범죄')
Genre.objects.create(title = '스릴러')
Genre.objects.create(title = 'SF')
Genre.objects.create(title = '무협')
Genre.objects.create(title = '첩보')
Genre.objects.create(title = '재난')

# 5 Queryset 메소드 `all` 을 활용해서 `Director` 테이블의 모든 데이터를
#  출력하는 코드를 작성하세요.
info = Director.objects.all()
for v in info:
    print(v.name,v.debut,v.country)

# 6 id가 1인 데이터 출력
info = Director.objects.get(id=1)
print(info.name,info.debut,info.country)

# 7 Queryset 메소드 `get` 을 활용해서 `Director` 테이블에서 `country` 가
#  USA인 데이터를 출력하는 코드를 작성하세요.
Director.objects.get(country='USA')


# 8 오류 메세지
# DoesNotExist                              Traceback (most recent call last)   
# Input In [73], in <cell line: 1>()
# ----> 1 Director.objects.get(country='USA')

# File ~\OneDrive\바탕 화면\TIL\DB\ORM\DB-ORM-master\venv\lib\site-packages\django\db\models\manager.py:85, in BaseManager._get_queryset_methods.<locals>.create_method.<locals>.manager_method(self, *args, **kwargs)
#      84 def manager_method(self, *args, **kwargs):
# ---> 85     return getattr(self.get_queryset(), name)(*args, **kwargs)        

# File ~\OneDrive\바탕 화면\TIL\DB\ORM\DB-ORM-master\venv\lib\site-packages\django\db\models\query.py:496, in QuerySet.get(self, *args, **kwargs)
#     494     return clone._result_cache[0]
#     495 if not num:
# --> 496     raise self.model.DoesNotExist(
#     497         "%s matching query does not exist." % self.model._meta.object_name
#     498     )
#     499 raise self.model.MultipleObjectsReturned(
#     500     "get() returned more than one %s -- it returned %s!"
#     501     % (
#    (...)
#     504     )
#     505 )

# DoesNotExist: Director matching query does not exist.
#이유 
# USA가 없어서 나오는 것 같음#

# 9 
 change = Director.objects.get(name='Joseph Kosinski')

 change.name
 #'Joseph Kosinski'

 change.country
 #'KOR'

 change.country = 'USA'

 change.save()

 Director.objects.get(country='USA')
 #<Director: Director object (7)>

 info = Director.objects.get(country='USA')
 print(info.name,info.debut,info.country)
# Joseph Kosinski 1999-01-01 00:00:00 USA

# 10
Director.objects.get(country='KOR')

# 12
info = Director.objects.filter(country='KOR')
for v in info:
    print(v.name, v.debut, v.country)


# 14 철수 지우기
del_ = Director.objects.get(name='김철수')
del_.delete()