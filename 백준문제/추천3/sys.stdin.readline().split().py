import sys #2020.08.15 입력
year, month, day = sys.stdin.readline().strip().split('.')
print(day + "-" + month + "-" + year)

year, month, day = sys.stdin.readline().split('.')
print(day + "-" + month + "-" + year)
# 아래코드는 strip 함수를 호출하지 않아서 day변수가 값과 개행을 
#함께 받게 된다. 그래서 결과는
# 15
#-08-2020
#이런식으로 개행과 함께 출력되기 때문에 위 코드와 같이 strip으로
#공백(개행,띄어쓰기)을 지워야 한다.