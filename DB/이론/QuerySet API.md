# QuerySet API

> __ 언더바 두개는 메서드를 호출하여 사용하는 방법이라고 생각하면 된다.

**gt**

```python
Entry.objects.filter(id__gt=4) # python
```

```sql
select * from Entry where id > 4;  # sql
```

같은 값을 나타냄

**gte**

```python
Entry.objects.filter(id__gte=4)
```

```sql
select * from Entry where id >= 4;
```



**lt**

```python
Entry.objects.filter(id__lt=4)
```

```sql
select * from Entry where id < 4;
```



**lte**

```python
Entry.objects.filter(id__lte=4)
```

```sql
select * from Entry where id <= 4;
```



**in**

```python
Entry.objects.filter(id__in=[1,3,4])
Entry.objects.filter(headline__in='abc')
```

```sql
select * from Entry where id in (1,3,4);
select * from Entry where headline in ('a','b','c');
```



**startswith**

```python
Entry.objects.filter(headline__startswith='Lennon')
```

```sql
select * from Entry where headline LIKE 'Lennon%';
```

Lennon으로 시작한다는 뜻



**endswith**

```python
Entry.objects.filter(headline__endswith='Lennon')
Entry.objects.filter(headline__iendswith='Lennon')
```

```sql
select * from Entry where headline LIKE '%Lennon';
select * from Entry where headline ILIKE '%Lennon';
--I는 대소문자 구분 안 한다는 의미
```



**contains**

```python
Entry.objects.get(headline__contains='Lennon')
Entry.objects.get(headline__icontains='Lennon')
```

```sql
select * from Entry where headline LIKE '%Lennon%';
select * from Entry where headline ILIKE '%Lennon%';
```



**range**

```python
import datetime
start_date = datetime.date(2005,1,1)
end_date = datetime.date(2005,3,31)
Entry.objects.filter(pub_date__range=(start_date, end_date))
```

```sql
select ... where pub_date
between '2005-01-01' and '2005-03-31';
```







## 용어 정리

| 용어            | 기능                       |
| --------------- | -------------------------- |
| gt              | > 초과                     |
| gte             | >= 이상                    |
| lt              | < 미만                     |
| lte             | <= 이하                    |
| in              | 포함                       |
| istartswith     | 대소문자 구분X             |
| endwith         |                            |
| contains        | 포함                       |
| range           | between A and B 와 같음    |
| order_by('-id') | id를 내림차순 정렬(python) |

```sql
select blog
from Entry
where

```



## ORM 확장 (1:M)



### Foreign Key (외래키)

- 키를 사용하여 부모 테이블의 유일한 값을 참조 (참조 무경성)
  - 데이터베이스 관계 모델에서 관련된 2개의 테이블 간의 일관성
- 외래 키의 값이 반그시 부모 테이블의 기본 키일 필요는 없지만 유일한 값이어야 함



### models.ForeignKey 필드

- 2개의 필수 위치 인자
  - Model class : 참조하는 모델
  - on_delete : 외래 키가 참조하는 객체가 삭제되었을 때 처리 방식
    - CASCADE :부모 객체가 삭제 됐을 때 이를 참조하는 객체도 삭제
    - PROTECT : 삭제되지 않음
    - SET_NULL : NULL 설정
    - SET_DEFAULT : 기본 값 설정

```	python
#참조
album = Album.objects.get(id=1)
album.artist # 앨범에 있는 아티스트 출력
#역참조
genre = Genre.objects.get(id=1)
genre.album_set.all()
# 장르를 가지고있는 모든 앨범 출력
```

