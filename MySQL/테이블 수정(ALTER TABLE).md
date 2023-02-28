# 테이블 수정(ALTER TABLE)

> 테이블 수정은 자주 사용할 예정이니 기록해두자.
>
> 사용 문법은 ALTER TABLE - 추가/변경/수정/삭제 모두 가능하다.
>
> 그 외 많은 것이 가능하지만 여기서는 추가/삭제/수정/변경을 다뤄본다.
>
> ✔️제약 조건이 있는 열은 수정에 주의를 기울여야 한다. 선행 작업이 필요함. 



## 열의 추가

- 사용 예시

```mysql
USE tabledb;
ALTER TABLE tabledb;
	ADD age INT -- 열 추가
		DEFAULT 1 -- 기본값 지정
		NOT NULL	-- NULL 
		FIRST; -- 가장 첫 열에 추가
        
```

추가 위치를 `FIRST`대신 특정 열에 추가하고 싶다면 `ALTER 열_이름` 하면 해당 열의 다음 칸에 추가된다.





## 열 삭제

- 사용 예시

``` mysql
ALTER TABLE usertbl
	DROP COLUMN email;
```

✔️만약 해당 열에 제약 조건이 있다면 먼저 제약 조건을 삭제해야 한다.





## 열 이름 및 테이블 형식 변경

- 사용 예시

``` mysql
ALTER TABLE usertbl
	CHANGE COLUMN name userName VARCHAR(15) NULL;
```

위 SQL문은 name이라는 열 이름을 userName으로 변경한 것이다. 추가로 형식도 입력한다.





## 열의 제약 조건 추가 및 삭제

- 사용 예시

```mysql
ALTER TABLE usertbl
	DROP PRIMARY KEY;
-- 만약 기본키가 참조되고 있다면 이 또한 외래 키를 삭제 후 기본 키를 삭제할 수 있다. 
ALTER TABLE usertbl
	DROP FOREIGN KEY buytbl;
```

