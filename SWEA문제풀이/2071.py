from audioop import avg
import sys
sys.stdin = open('2071.txt', 'r')


t = int(input())

for case in range(1,t+1):

    a=list(map(int, input().split()))
    result = sum(a) / 10
    print(f'#{case}',format(int(round(result, 0))))