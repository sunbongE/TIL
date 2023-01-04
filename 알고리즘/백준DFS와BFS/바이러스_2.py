def dfs(x):
    global ans
    ans += 1
    v[x] = 1
    for n in arr[x]:
        if not v[n]:
            v[n] = 1
            dfs(n)

N = int(input())    
q=[]

arr=[[] for _ in range(N+1)]
v=[0] * (N+1)

for _ in range(int(input())):
    s,e = map(int,input().split())
    arr[s].append(e)
    arr[e].append(s)
ans=0
dfs(1)    
print(ans-1)