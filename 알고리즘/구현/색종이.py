n =int(input()) 
from pprint import pprint
arr = [[0]*101 for _ in range(101)]

for _ in range(n):
    x,y = map(int,input().split())

    for i in range(x,x+10):
        for j in range(y,y+10):
            arr[i][j] = 1
ans = 0
for ar in arr:
    ans += ar.count(1)
print(ans)

#다른 풀이
points = [[0 for i in range(100)] for j in range(100)]
n = 0
cnt = int(input())
for z in range(cnt):
    x, y = map(int, input().split())
    for i in range(x-1, x+9):
        for j in range(y-1, y+9):
            if points[i][j] == 0:
                points[i][j] = 1
                n += 1

print(n)