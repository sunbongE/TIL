# 파이썬과 연결(pymysql)

mysql과 python을 연결하려면 pymysql을 설치한다.

```bash
pip install pymysql
```



### MySQL에 데이터 입력 순서(INSERT)

1. MySQL연결

   ```python
   import pymysql
   연결자_변수 = pymysql.connect(연결옵션)
   # 연결옵션 => host='127.0.0.1', user='root', password='????', db='UR_DB',charset='utf8' 등등
   ```

2. 커서 생성
   ```python
   커서_변수 = 연결자_변수.cursor()
   ```

3. 테이블 생성 or 데이터 입력
   ```python
   커서_변수.execute("SQL문")
   ```

4. 입력한 데이터 저장
   ```python
   연결자_변수.commit()
   ```

5.  MySQL 종료
   ```python
   연결자_변수.close()
   ```

6. 실습 코드
   ```python
   import pymysql
   
   conn, cur = None, None
   data1, data2, data3, data4 = "", "", "", ""
   sql = ""
   
   # main code
   
   # 1. 연결자 생성
   conn = pymysql.connect(
       host="127.0.0.1", user="root", password="1234", db="hanbitDB", charset="utf8"
   )
   # 2. 커서 생성
   cur = conn.cursor()
   
   # 3. 테이블 생성
    sql = "CREATE TABLE IF NOT EXISTS userTable (id char(4), userName char(15), email char(20), birthYear int)"
    cur.execute(sql)
   
   # 4. 데이터 입력
   while True:
       data1 = input("사용자 ID ==> ")
       if data1.strip() == "":
           break
       data2 = input("사용자 이름 ==> ")
       data3 = input("사용자 이메일 ==> ")
       data4 = input("사용자 출생연도 ==> ")
       sql = (
           "INSERT INTO userTable VALUES("
           + data1
           + ","
           + data2
           + ","
           + data3
           + ","
           + data4
           + ")"
       )
   
       cur.execute(sql)
   
       conn.commit()
       conn.close()
   
   ```

   

### MySQL에 데이터 조회 순서(SELECT)

1. MySQL연결

   ```python
   import pymysql
   연결자_변수 = pymysql.connect(연결옵션)
   # 연결옵션 => host='127.0.0.1', user='root', password='????', db='UR_DB',charset='utf8' 등등
   ```

2. 커서 생성

   ```python
   커서_변수 = 연결자_변수.cursor()
   ```

3. 데이터 조회

   ```python
   커서_변수.execute("SELECT ...")
   ```

4. 조회한 데이터 출력
   ```python
   커서_변수.fetchone()
   ```

5. MySQL 종료
   ```sql
   연결자.close()
   ```

6. 실습 코드
   ```python
   import pymysql
   
   # 전역 변수 선언부
   conn, cur = None, None
   
   data1, data2, data3, data4 = "", "", "", ""
   
   row = None
   
   # main code
   # 1. 연결자 생성
   conn = pymysql.connect(
       host="127.0.0.1", user="root", password="1234", db="hanbitDB", charset="utf8"
   )
   
   # 2. 커서 생성
   cur = conn.cursor()
   # 3. 데이터 조회
   cur.execute("select * from userTable")
   
   # 4. 데이터 출력
   print("사용자ID  사용자이름  이메일    출생연도")
   print("-----------------------------------------")
   
   while 1:
       row = cur.fetchone()
       if row == None:
           break
       data1, data2, data3, data4 = row
       print("%5s %15s %15s %d" % (data1, data2, data3, data4))
   
   ```

   

