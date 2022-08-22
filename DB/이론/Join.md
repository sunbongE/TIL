# Join

- 관계형 데이터베이스의 가장 큰 장점이자 핵심적인 기능
- 일반적으로 데이터베이스에는 하나의 테이블에 많은 데이터를 저장하는 것이 아니라 여러 테이블로 나눠 저장하게 되며, 여러 테이블을 결합하여 출력하여 활용
- 일반적으로 레코드는 기본 키 또는 외래 키 값의 관계에 의해 결합함

 

INNER JOIN : 두 테이블에 모두 일치하는 행만 반환

```sqlite
SELECT * 
FROM 테이블1 [INNER] JOIN 테이블2
	ON 테이블1.컬럼 = 테이블2.컬럼;
-- INNER은 생략가능
```



OUTER JOIN : 동일한 값이 없는 행도 반환

```sqlite
SELECT * 
FROM 테이블1 [LEFT,RIGHT,FULL] OUTER JOIN 테이블2
	ON 테이블1.컬럼 = 테이블2.컬럼;
```



CROSS JOIN : 모든 데이터의 조합

```sqlite
SELECT *
FROM 테이블1 CROSS JOIN 테이블2;
```

