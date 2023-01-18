import sys
sys.setrecursionlimit(10000)
def dfs(start):
    v[start]=1
    
    for i in arr[start]:
        if not v[i]:
            dfs(i)


N,M = map(int,input().split())
cnt=0
v=[0]*(N+1)
v[0]=1
arr=[[] for _ in range(N+1)]
for _ in range(M):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
for i in range(len(v)):
    if v[i] == 0 :
        dfs(i)
        cnt+=1

print(cnt)