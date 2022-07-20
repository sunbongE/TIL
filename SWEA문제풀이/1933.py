# 입력으로 1개의 정수 N 이 주어진다.

# 정수 N 의 약수를 오름차순으로 출력하는 프로그램을 작성하라.
#10
#1,2,5,10

n=int(input())
for i in range(1,n+1):
    if n % i == 0:
        print(i,end=' ')
