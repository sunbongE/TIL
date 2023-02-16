# MySQL 변수

변수는 Workbench를 닫으면 소멸한다.(1회용)



형식

```mysql
SET @변수이름 = 변수의 값 ;	-- 값을 할당
SELECT @변수이름 ;			-- 출력
```



```mysql
-- 변수
use sqldb
set @Var1 = 5;
set @Var2 = 100;
set @Var3 = 3.14;
set @Var4 = 'Hell' ;


SELECT @Var1 + @Var2;
SELECT @Var3;
SELECT @Var4 + @Var3; -- 문자를 연산할때 0으로 취급한다.

```



### PREPARE와 EXECUTE

FROM절에 변수로 LIMIT을 사용하는 것은 안되는데 그것을 가능하게 하기 위해서는 

아래와 같은 문법을 사용한다.

```mysql
SET @var1 = 3;
PREPARE myQuery
	from 'SELECT Name, height FROM usertbl ORDER BY height LIMIT ?';
EXECUTE myQuery USING @var1 ; 
-- EXECUTE A using var -> A의 ? 에 var가 사용된다.
```

