# 하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.

n = int(input())
result = 0
while n:
    
    result += (n % 10)
    n //= 10
print(result)