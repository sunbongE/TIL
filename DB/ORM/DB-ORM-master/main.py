import sys
import os
import django
sys.dont_write_bytecode = True
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from db.models import *

# 아래에 코드를 기록하세요.
# 코드 실행은 터미널에서 shell을 실행시켜서 해주세요. 
# $ python manage.py shell_plus 

# 1. 데이터 전체 조회
Genre.objects.all()
#<QuerySet [<Genre: Genre object (1)>, <Genre: Genre object (3)>]>

#2. 일부 데이터 조회 get
Genre.objects.get(id=1)
#<Genre: Genre object (1)>  값이 1개(Primary Key), 값이 없거나 많으면 오류 출력

#3. 일부데이터 조회 filter
Genre.objects.filter(id=3)
#<QuerySet [<Genre: Genre object (3)>]>


# delete
# 1. genre 객체 활용
genre = Genre.objects.get(id = 4)
# 2. genre 객체 삭제
genre.delete()
#(1, {'db.Genre': 1})