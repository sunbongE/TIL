import sys

sys.stdin = open('2072.txt', 'r')

t = int(input())

for i in range(1,t+1):
    result = 0
    a = list(map(int, input().split()))
    for j in a:
        if j % 2 == 1:
            result += j

    print(f'#{i} {result}')