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
# sql = "CREATE TABLE IF NOT EXISTS userTable (id char(4), userName char(15), email char(20), birthYear int)"
# cur.execute(sql)

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
