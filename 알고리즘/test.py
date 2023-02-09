def dfs(start)  :
    ans.append(start)
    v[start] = 1
    for i in arr[start]:
        if not v[i]:
            dfs(i)

def bfs(start):
    v[start]=1
    p=[]
    p.append(start)
 
    while p:
        cur = p.pop(0)
        ans.append(cur)

        for i in arr[cur]:
            if not v[i]:
                v[i] = 1
                p.append(i)

N,M,V = map(int,input().split())

arr = [[] for _ in range(N+1)]
# print(arr)

for _ in range(M):
    a,b = map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)

for ar in arr:
    ar.sort()
# print(arr) 
# # [[], [2, 3, 4], [1, 4], [1, 4], [1, 2, 3]]

v = [0]*(N+1)
v[0] = 1
ans=[]
dfs(V)
print(*ans)
v = [0]*(N+1)
v[0] = 1
ans=[]
bfs(V)
print(*ans)