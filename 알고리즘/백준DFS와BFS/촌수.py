from collections import deque

def bfs(start):
    global cnt,a,b
    v[start] = 1    #시작한거 방문처리해주고
    q.append(start) # q에 넣어줌

    while q :
        if v[a] and v[b]: # 둘다 방문했을 때
            return cnt
        cnt += 1
        cur = q.popleft()
        for t in arr[cur]:
            if not v[t]:
                v[t] =1 
                q.append(t)
    else: cnt = -1 ; return cnt # if문 안걸리면 요거

cnt = 0
n = int(input())
q=deque()
a,b = map(int,input().split())
arr = [[] for _ in range(n+1)]
v = [0] * (n+1)
for _ in range(int(input())):
    x,y = map(int,input().split())  
    arr[x].append(y)
    arr[y].append(x)
bfs(a)
print(cnt)
