import sys

input = sys.stdin.readline
M, N = map(int, input().split())


for num in range(M, N + 1):
    if num == 1:
        continue
    for j in range(2, int(num**0.5) + 1):
        if num % j == 0:
            break
    else:
        print(num)

        
# 빠른 풀이
m,n=map(int,input().split())

arr = [True]*(n+1) #리스트 생성
arr[0] = False
arr[1] = False

for i in range(2,int(n**0.5)+1): #2부터 n의 제곱근까지
    if arr[i]: #i가 남은 수인 경우
        for j in range(i*2,n+1,i): #range(start, stop, step)
            arr[j] = False
            
#소수 출력            
for i in range(m,n+1):
    if arr[i]:
        print(i)