from collections import deque
# dfs 들어가면 방문처리하고 반복문으로 배열을 돌려서 방문안된 애들은 다시 재귀호출로 보내
# bfs 들어가면 방문처리하고 큐에 담아서 큐에 값이 있는 동안 큐안에 있는
# 값들을 순회하면서 방문처리 안돼있으면 방문까지만 하고 돌아와야
# 직결된 애들만 조회를 하고 넘어온 것이다.
# 그런다음 for문이 끝나면 큐에 남아있는 방금 방문한 친구를 뽑아서
# 다시 그 배열을 순회하여 그친구와 직결된 애들을 방문안되어 있는 애들은 방문하면서
# 큐에 삽입하는 이런 과정을 큐에 값이 없을 때까지 반복하는 것이다.#
# def dfs(a):
#     v[a]=1 #방문처리
#     dfs_ans.append(a)
    
#     for x in arr[a]:
#         if not v[x]:
#             v[x]=1
#             dfs(x)
def dfs(a):
    v[a]=1
    dfs_ans.append(a)
    for x in arr[a]:
        if not v[x]:
            v[x]=1
            dfs(x)



# def bfs(b):
#     v[b]=1
#     q=deque()
#     q.append(b)
#     bfs_ans.append(b)
#     while q:
#         c = q.popleft()
#         for j in arr[c]:
#             if not v[j]:
#                 q.append(j)
#                 bfs_ans.append(j)
#                 v[j]=1
def bfs(b):
    v[b]=1
    q=deque()
    q.append(b)
    bfs_ans.append(b)

    while q:
        cur = q.popleft()
        for y in arr[cur]:
            if not v[y]:
                v[y]=1
                bfs_ans.append(y)
                q.append(y)   




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
# print(arr)

dfs(start)
print(*dfs_ans)

v=[0]*(N+1)

bfs(start)
print(*bfs_ans)