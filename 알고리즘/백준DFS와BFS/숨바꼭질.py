from collections import deque
def bfs(s,e):
    global cnt
    q=deque()
    q.append(s)
    v=[0]*100001
    v[s]=1
    while q:
        cur = q.popleft()
        if cur == e:
            return v[e]-1

        for x in (cur*2, cur-1, cur+1):
            if 0<=x<100001 and not v[x]:
                q.append(x)
                v[x] = v[cur] + 1

    return -1

cnt = 0
subin, sister = map(int,input().split())    
ans = bfs(subin, sister)
print(ans)