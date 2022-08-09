
import sys
sys.stdin = open('얼마.txt','r')
# 2 케이스
# 10000  차 가격
# 2        n개 반복입력 옵션개수
# 1 2000        q옵션개수   p가격 
# 3 400    1200     
# 50000     차 가격
# 0 옵션개수 
T = int(input())

for _ in range(T):
    car_price = int(input())
    op = int(input())
    add_price = 0
    for _ in range(op):
        c, p = map(int, input().split())
        add_price += c*p
    print(car_price+add_price)