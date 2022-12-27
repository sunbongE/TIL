def dfs(c):
    global ans
    ans += 1 #
    v[c] = 1 #방문처리
    for n in arr[c]: # c와 연결된 노드 모두 처리
        if not v[n]: # 방문하지 않은 노드는 재귀호출
            dfs(n)
            # 재귀호출을 통해서 방문 안된 노드를 계속 파고 드니까 깊이 우선 탐색인듯 하다.



N = int(input())
arr =[[] for _ in range(N+1)]
v =  [0]*(N+1)
for _ in range(int(input())):
    s,e= map(int,input().split())
    arr[s].append(e)
    arr[e].append(s)
ans = 0 # 연결된 노드의 개수를 기록할 예정
dfs(1)
print(ans-1)