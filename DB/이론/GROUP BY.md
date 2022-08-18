# GROUP BY

- select 문optional 절
- 행 집합에서 요약 행 집합을 만듬
- 선택된 행 그룹을 하나 이상의 열 값으로 요약 행으로 만듬
- 문장에 where 절이 포함된 경우 반드시 **where절 뒤에 작성**

```sqlite
SELECT * FROM 테이블 GROUP BY 컬럼1, 컬럼2;
```

- 지정된 컬럼의 값이 같은 행들로 묶음
- 집계 함수와 활용하였을 때 의미 있다,
- 그룹화된 각각의 그룹이 하나의 집합으로 집계 함수의 인수로 넘겨짐
- 명시되지 않은 컬럼은 별도로 지정 못함
  - 그룹마다 하나의 행을 출력하게 되므로 집계 함수 등을 활용해야한다.
- **결과는 정렬되지 않음**
  - 기존의 순서와 바뀌는 모습도 있음
  - 원칙적으로 관계형 데이터베이스에서 ORDER BY로 정렬한다. 



### Aggregate function (집계 함수) 다시 보기

- 값 집합에 대한 계산을 수행하고 단일 값을 반환
- 여러 행으로부터 하나의 결과 값을 반환

- SELECT 구문에서만 사용함
  - ex) count(*), avg(age)



## ALIAS	

-  칼럼 명이나 테이블 명이 너무 길거나 다른 명칭으로 확인하고 싶으면 사용
- AS를 생략해 공백으로 표현 가능
  - ex) SELECT last_name 성 FROM ~~~~
- 별칭에 공백, 특수 문자 등이 있는 경우 따옴표로 묶어서 표기

![image-20220818142048955](GROUP%20BY.assets/image-20220818142048955.png)



## HAVING

집계 함수는 WHERE 절의 조건식에서는 사용할 수 없음 (실행 순서가 더 빠르기 때문)

집계 결과에서 조건에 맞는 값을 따로 활용하기 위해서 HAVING을 활용

```sqlite
SELECT * FROM 테이블 GROUP BY 컬럼1, 컬럼2 HAVING 그룹조건;

실행 순서
FROM - WHERE - GROUP BY - HAVING - SELECT - ORDER BY
```





## ALTER TABLE

1.  테이블 이름 변경
2.  새로운 column 추가
3.  column 이름 수정
4.  column 삭제

```sqlite
-- 1.
ALTER TABLE table_name
RENAME TO new_name;

-- 2.
ALTER TABLE table_name
ADD COLUMN column_definition;

--3.
ALTER TABLE table_name
RENAME COLUMN current_name TO new_name;

--4. 
ALTER TABLE table_name
DROP COLUMN current_name ;
```

