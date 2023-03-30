import sys

input = sys.stdin.readline

n = int(input())
xy = [list(map(int, input().split())) for _ in range(n)]
xy.sort(key=lambda x: (x[1], x[0]))
for i in xy:
    print(*i)
