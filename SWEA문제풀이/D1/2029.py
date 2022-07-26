import sys
sys.stdin = open("2029.txt","r")
# 2개의 수 a, b를 입력 받아, a를 b로 나눈 몫과 나머지를 출력하는 프로그램을 작성하라.

t = int(input())

for case in range(1,t+1):
    a, b= map(int, input().split())

    print(f'#{case} {a//b} {a%b}')
