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

# 데이터 출력
print("사용자ID  사용자이름  이메일    출생연도")
print("-----------------------------------------")

while 1:
    row = cur.fetchone()
    if row == None:
        break
    data1, data2, data3, data4 = row
    print("%5s %15s %15s %d" % (data1, data2, data3, data4))
