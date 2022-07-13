# 정수 2개(a, b)를 입력받아 a를 2b배 곱한 값으로 출력해보자.
# 0 <= a <= 10, 0 <= b <= 10
a, b = map(int, input().split())
b = 2**b
print(a*b)
