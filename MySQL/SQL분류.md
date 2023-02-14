# SQL 분류

## DML(Data Manipulation Language) 데이터 조작 언어

> 트랜잭션 : 테이블의 데이터를 조작했을 때 완전히 적용되지 않고 임시로 적용하는 것이다.
> (실수했을 때 임시 적용된 것을 취소할 수 있다.)

데이터를 조작(선택, 삽입, 수정, 삭제)하는 언어, 트랜잭션이 발생한다.

- SELECT
- INSERT
- UPDATE
- DELETE

## DDL(Data Definition Language) 데이터 정의 언어

DB, Table, 뷰, 인덱스 등의 데이터베이스 개체를 생성, 삭제, 변경하는 언어

- CREATE
- DROP
- ALTER

트랜잭션이 발생하지 않아서 SQL실행 즉시 적용된다. 임시 적용이 없으므로 실수했을 때 돌이킬 수 없다.

## DCL(Data Control Language) 데이터 제어 언어

사용자의 권한을 부여, 회수하는 언어

- GRANT
- REVOKE
- DENY

