# CASE

- 특정 상황에서 데이터를 변환하여 활용 가능
- ELSE를 생략하는 경우 NULL이 지정됨

```sqlite
select --select 안에 있어야함
    case
        when 조건식 then 식
        when 조건식 then 식
        else 식 
    end AS 별명
```



# 서브 쿼리

- 서브 쿼리는 특정한 값을 메인 쿼리에 반환하여 활용하는 것
- 실제 테이블에 없는 기준을 이용한 검색이 가능
- 서브 쿼리는 소괄호로 감싸서 사용하며, 메인 쿼리의 칼럼을 모두 사용할 수 있음
- 메인 쿼리는 서브 쿼리의 칼럼을 이용할 수 없음







### 단일 행 서브 쿼리

- 서브 쿼리의 결과가 0 또는 1 개 경우
- 단일행 비교 연산자와 함께 사용(=,<,<=,>,>=,<>)

```sqlite
select count(*)
from users
where age = (select min(age) from users); -- 괄호 안에 넣어서 서브쿼리 표현
```

```sql
-- 평균 잔고보다 높은 사람 수
select count(*)
from users
where balance > (select avg(balance) from users);
```



### 다중 행 서브 쿼리

- 서브 쿼리 결과가 2개 이상인 경우
- 다중 행 비교 연산자와 함께 사용(IN, EXISTS 등)



### 다중 칼럼 서브 쿼리





