import sys
input = sys.stdin.readline
def dfs(c):
    ans_dfs.append(c) # 방문 노드 추가
    print(c,end=' ')
    v[c]=1              # 방문 표시

    for n in adj[c]:
        if not v[n]: # 방문하지 않은 노드인 경우
            dfs(n)

def bfs(s):
    q=[]            #필요한 q, v 변수 생성
    q.append(s)     #초기데이터 삽입

    # ans_bfs.append(s)
    print(s,end=' ')
    v[s]=1
    while q:
        c = q.pop(0)    
        for n in adj[c]:
            if not v[n]:    #방문 안한 노드라면 큐 삽입
                q.append(n)
                # ans_bfs.append(n)
                print(n,end=' ')

                v[n]=1





N,M,V = map(int,input().split())
adj = [[] for _ in range(N+1)]

for _ in range(M):
    s,e = map(int,input().split())
    adj[s].append(e)
    adj[e].append(s) # 양방향 입력
# print(adj)
# 오름차순 정렬
for i in range(1,N+1)   :
    adj[i].sort()

v = [0]*(N+1)
ans_dfs=[]
dfs(V)
print()
v = [0]*(N+1)
ans_bfs=[]
bfs(V)
# print(*ans_dfs)
# print(*ans_bfs)
