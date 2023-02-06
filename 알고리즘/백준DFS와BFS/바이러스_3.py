def dfs(start):
    global cnt
    cnt += 1
    v[start]=1

    for i in com[start]:
        if not v[i]:
            dfs(i)

n = int(input())
m=int(input())
com = [[] for _ in range(n+1)]

v=[0]*(1+n)
v[0]=1
for _ in range(m):
    a,b = map(int,input().split())
    com[a].append(b)
    com[b].append(a)
cnt=0
dfs(1)
print(cnt-1)
