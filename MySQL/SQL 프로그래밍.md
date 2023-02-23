# SQL 프로그래밍

MySQL에서 "if, case, while"과 같은 프로그래밍 기능을 사용하는 방법과 "동적 SQL"에 대해서 알아보겠습니다.

>먼저, "if, case, while"과 같은 **프로그래밍 기능**을 **사용하기 위해서**는 **스토어드 프로시저를 사용해야 합니다.** 
>스토어드 프로시저는 데이터베이스 개체로, SQL 프로그래밍을 할 때 기본적으로 사용됩니다. 

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
> 한 문장 이상이 처리되어야 하면 BEGIN... END로 묶어야 합니다.

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

> if문보다 깔끔하게 보일 수 있다는 장점이 있습니다.

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





### WHILE..DO

> 반복문
>
> ITERATE : 다시 WHILE문으로 올라가는 역학 , 파이썬으로 치면 continue 입니다.
>
> LEAVE : 반복문을 빠져나가는 역할입니다.

- while문 사용 예시

```mysql
WHILE (condition) DO
    -- code block
END WHILE;

```



### 오류 처리

> MySQL에서 오류가 발생했을 때 처리하는 방법을 지원합니다.

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
  - 오류 발생 시 행동을 정의하는데 CONTINUE, EXIT 중 하나를 사용합니다.
    - CONTINUE - "처리할 문장"을 실행합니다.
    - EXIT - 해당 저장 프로시저 내부에서 실행을 중단하고, 프로시저를 빠져나오는 역할을 합니다.

- 오류 조건
  - 어떤 오류를 처리할지 지정합니다.
    - 서버 오류 : 1000~1906, 3000~3186까지 정의되어있습니다.
    - 클라 오류 : 2000~2062까지 정의되어있습니다
- 처리할 문장
  - 문장이 하나면 한 문장, 여러 개면 BEGIN ~ END으로 묶어야 합니다.



### 동적 SQL

> 미리 쿼리문을 준비한 후에 나중에 실행하는 것을 동적 SQL이라고 합니다.

- STEP

1. PREPARE - SQL문을 실행하지 않고 미리 준비만 합니다.
2. EXECUTE - 준비된 쿼리문을 실행합니다.
3. 실행 ...
4. DEALLOCATE PREFARE - 할당을 해제합니다.

- prepare, execute, deallocate를 사용한 동적 SQL 사용 예시

```mysql
PREPARE  myquery from 'select * from usertbl where userid = ?';	-- 준비
EXECUTE  myquery using @userid;	-- 실행
DEALLOCATE PREPARE myquery;		-- 사용한 문장을 해제한다.
```



---

### case 실습

리눅스 환경에서 실습

usertbl, buytbl 조인하여 전체 고객들의 총구매액 기준으로 등급을 나누는 쿼리

![image-20230223131615289](SQL%20%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%B0%8D.assets/image-20230223131615289.png)

(마우스가 안되니까 오타 수정하는게 힘들다. 마우스 고마워)



### while .. do 실습

1~1000 숫자 중 3 or 8 배수만 합한 값을 구하는 스토어드 프로시저를 만들어보자.

ITERATE, LEAVE 사용한 코드

```mysql
-- 1~1000중 3,8배수만 더한 값 while문
DELIMITER $$
CREATE PROCEDURE sum_multiples()
BEGIN
		DECLARE i INT;	-- 변수 선언
        DECLARE hap INT;
	
	SET i = 0;			-- 변수에 값 할당
    SET hap = 0;
    
		label: WHILE (i <= 1000) DO -- 라벨을 지정한다.
			SET i = i + 1; -- 1 증가
			IF (i%3=0) OR (i%8=0) THEN 	-- 3이나8의 배수라면
				SET hap = hap + i;		-- HAP에 I를 더한다.
                ITERATE label; 			-- ITERATE은 지정한 라벨로 돌려보내 실행시키는 역할이다.
			END IF;
            
            IF (i > 1000) THEN			-- I변수가 1000을 넘어가면
				LEAVE label;			-- 라벨을 멈춘다.
			END IF ;
            END WHILE;
	SELECT hap;
END $$
DELIMITER ;
CALL sum_multiples();
```

위에서 ITERATE와 LEAVE 역할을 이해하기 위해 사용했지만 더 짧은 코드가 있습니다.

```mysql
-- 1~1000중 3,8배수만 더한 값 while문 2
DELIMITER $$
CREATE PROCEDURE sum_multiples()
BEGIN
  DECLARE i INT DEFAULT 1; -- 변수할당 및 초기화
  DECLARE total INT DEFAULT 0;
  WHILE i <= 1000 DO		-- WHILE은 I가 1000보다 커지면 종료된다.
    IF i % 3 = 0 OR i % 8 = 0 THEN
      SET total = total + i;
    END IF;
    SET i = i + 1;
  END WHILE;
  SELECT total;
END$$
DELIMITER ;
call  sum_multiples();
```



### 오류 핸들링 실습

문법이 많아서 다소 헷갈리만 해석을 해보면 기억하기 쉽습니다.

DECLARE(선언하다) CONTINUE(계속하다) HANDLER FOR ???.. 
???을 어떤걸로 계속하도록 선언한다 라고 생각하면 쉬워집니다.

```mysql
-- 오류처리
DROP PROCEDURE IF EXISTS errorProc;
DELIMITER $$
CREATE PROCEDURE errorProc()
BEGIN
	DECLARE CONTINUE HANDLER FOR 1146 SELECT 'NULL TABLE' AS 'MESSAGE';
	-- 1146에러가 발생하면 NULL TABLE을 출력하고 SQL계속 실행하도록 선언한다!
    SELECT * FROM noTable;
    SELECT '계속되나';	
END $$
DELIMITER ;
CALL errorProc();
```



### 동적SQL 실습

> 쿼리를 실행하는 순간의 날짜와 시간이 입력되는 기능

```mysql
    
-- 실행하는 순간의 날짜와 시간이 입력되는 기능 
DROP TABLE IF EXISTS myTable;
CREATE TABLE myTable (id INT AUTO_INCREMENT PRIMARY KEY, mDate DATETIME);

SET @curDATE = current_timestamp(); -- 현재 날짜와 시간
PREPARE myQuery FROM 'INSERT INTO myTable VALUES(NULL,?)';
EXECUTE myQuery USING @curDATE; -- @curDATE 변수가 ? 여기에 들어간다.
DEALLOCATE PREPARE myQuery;

SELECT * FROM myTable;

```



