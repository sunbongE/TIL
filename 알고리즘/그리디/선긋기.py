import sys
input = sys.stdin.readline

n = int(input())  
lines = [tuple(map(int,input().split())) for _ in range(n)]
lines.sort()
s = lines[0][0]
e = lines[0][1]

ans = 0
for i in range(1,n):
    if e >= lines[i][0]:
        e = max(e,lines[i][1])

    else:
        ans += e-s
        s = lines[i][0]
        e = lines[i][1]
ans += e-s
print(ans)
