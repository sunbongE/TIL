import sys
sys.stdin = open('1217.txt')

for _ in range(10):

    case = int(input())

    N,M = list(map(int, input().split()))

    print(f'#{case} {N**M}')