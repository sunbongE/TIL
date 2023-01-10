import sys
input = sys.stdin.readline
N = int(input())
li=[]   
cnt = 0
for _ in range(N):
    li.append(list(map(int,input().split())))
li.sort(key = lambda x : (x[1],x[0]))
b = li[0][1]
for i in range(1,N):
    if li[i][0] >= b:
        b = li[i][1]
        cnt += 1
print(cnt+1)