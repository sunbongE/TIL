# MySQL 잘 사용하기



## 데이터 베이스의 원칙

1. 무결성(integrity): 항상 정확해야함
2. 안정성 : 고장이 잘 안나야함
3. 확장성 : 데이터가 늘어나면 대비할 수 있어야함(Scale Up, Scale Out)

## 다양한 데이터베이스 종류

- RDBMS : 테이블 형태로 데이터를 저장
- Redis : Key-value형태로 데이터를 저장

- DynamoDB : Key-value인데 키가 2개로 나누어진 형태(Partition Key)

- graph : 연결된 구조 (1촌 2촌 등에 사용한다고함.)
- MongoDB (Document) : 저장되는 데이터의 형태가 자유롭다.

row oriented database

column oriented database

## CAP Theorem

consistency : 일괄처리 한번에 많은 데이터

Avail

Partition - ..

