from collections import deque
def dfs(a):
    v[a]=1 #방문처리
    dfs_ans.append(a)
    
    for x in arr[a]:
        if not v[x]:
            v[x]=1
            dfs(x)




def bfs(b):
    v[b]=1
    q=deque()
    q.append(b)
    bfs_ans.append(b)
    while q:
        c = q.popleft()
        for j in arr[c]:
            if not v[j]:
                q.append(j)
                bfs_ans.append(j)
                v[j]=1
        



dfs_ans=[]
bfs_ans=[]
N,M,start=map(int,input().split())

v=[0]*(N+1)
arr=[[] for _ in range(N+1)]
for _ in range(M):
    s,e = map(int,input().split())  
    arr[s].append(e)
    arr[e].append(s)
for i in range(N+1):
    arr[i].sort()
print(arr)

dfs(start)
print(*dfs_ans)

v=[0]*(N+1)

bfs(start)
print(*bfs_ans)