# SQL 프로그래밍

MySQL에서 "if, case, while"과 같은 프로그래밍 기능을 사용하는 방법과 "동적 SQL"에 대해서 알아보겠습니다.

먼저, "if, case, while"과 같은 프로그래밍 기능을 사용하기 위해서는 스토어드 프로시저를 사용해야 합니다. 스토어드 프로시저는 데이터베이스 개체로, SQL 프로그래밍을 할 때 기본적으로 사용됩니다. 스토어드 프로시저는 다음과 같은 형식을 갖습니다.

### 스토어드 프로시저

> SQL 쿼리 및 프로그래밍 언어를 사용하여 MySQL 서버에 저장된 일련의 SQL 문장 집합을 의미합니다. 

사용법 

```mysql
DELIMITER $$
CREATE PROCEDURE 스토어드_프로시저이름()
BEGIN
	
	 code block -- 프로그램 입력
	
END $$
DELIMITER ;
CALL 스토어드_프로시저이름(); -- 프로그램 실행
```



### IF ... ELSE

> 조건문
>
> 한 문장 이상이 처리되어야 하면 BEGIN... END로 묶어줘야 한다.

사용법

```mysql
IF 조건 THEN
	SQL문
ELSE 
	SQL문
END IF;

```



```mysql
DELIMITER $$ -- 스토어드 프로시저
CREATE PROCEDURE ifProc()
BEGIN  
	DECLARE var1 INT ; -- 변수 선언
    set var1 = 100;		-- 값 할당
    -- 조건문
    if var1 = 100 then
		select 'var1 == 100';
	else
		select 'var1 != 100';
	end if;
END $$ 
DELIMITER ;
CALL ifProc();
```



### CASE

> if문보다 깔끔하게 보일 수 있다는 장점이 있다.

- case문 사용 예시

```mysql
case expression
    when value1 then
        -- code block
    when value2 then
        -- code block
    else
        -- code block
end case;

```





### WHILE

> 반복문
>
> ITERATE : 다시 WHILE문으로 올라가는 역학 , 파이썬으로 치면 continue
>
> LEAVE : 반복문을 빠져나가는 역할

- while문 사용 예시

```mysql
while (condition) do
    -- code block
end while;

```



### 오류 처리

> MySQL에서 오류가 발생했을 때 처리하는 방법을 지원한다.

- 오류 처리 사용 예시

```mysql
DECLARE 액션 HANDLER FOR 오류조건 처리할 문장;

-- 적용 예시
BEGIN
	DECLARE CONTINUE HANDLER FOR 1146 SELECT '테이블이 없다' AS '오류 메시지';
	SELECT * FROM noTable; -- 없는 테이블 조회
END $$
```

- 액션
  - 오류 발생 시 행동을 정의하는데 CONTINUE, EXIT 중 하나를 사용한다.
    - CONTINUE - "처리할 문장"을 실행한다.
    - EXIT - 해당 저장 프로시저 내부에서 실행을 중단하고, 프로시저를 빠져나오는 역할을 한다.

- 오류 조건
  - 어떤 오류를 처리할지 지정한다.
    - 서버 오류 : 1000~1906, 3000~3186까지 정의
    - 클라 오류 : 2000~2062까지 정의
- 처리할 문장
  - 문장이 하나면 한 문장, 여러 개면 BEGIN ~ END으로 묶어야 한다.



### 동적 SQL

> 미리 쿼리문을 준비한 후에 나중에 실행하는 것을 동적 SQL이라고 한다.

- STEP

1. PREPARE - SQL문을 실행하지 않고 미리 준비만 시킨다.
2. EXECUTE - 준비된 쿼리문을 실행한다.
3. 실행 
4. DEALLOCATE PREFARE - 문장을 해제한다.

- prepare, execute, deallocate를 사용한 동적 SQL 사용 예시

```mysql
PREPARE  myquery from 'select * from usertbl where userid = ?';	-- 준비
EXECUTE  myquery using @userid;	-- 실행
DEALLOCATE PREPARE myquery;		-- 사용한 문장을 해제한다.
```

