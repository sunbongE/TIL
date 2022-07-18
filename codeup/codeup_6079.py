# 1, 2, 3 ... 을 계속 더해 나갈 때,
# 그 합이 입력한 정수(0 ~ 1000)보다 같거나 작을 때까지만
# 계속 더하는 프로그램을 작성해보자.

sum_t = 0
cn = 0
a = int(input())
while sum_t < a: #참 일때 멈춘다.
    cn += 1
    sum_t += cn

print(cn)