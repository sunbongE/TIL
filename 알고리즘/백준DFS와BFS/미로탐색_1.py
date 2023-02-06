def bfs(si,sj,ei,ej):
    p=[]
    p.append((si,sj))
    v = [[0]*M for _ in range(N)]

    while p:
        (ci,cj) = p.pop(0)
        if (ci,cj) == (ei,ej):
            return v[ei][ej]
        
        for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            if 0 <= ni < N and 0 <= nj < M and v[ni][nj] == 0 and arr[ni][nj] == 1:
                v[ni][nj] = v[ci][cj] + 1
                p.append((ni,nj))

N,M = map(int, input().split())

arr = []

for _ in range(N):
    arr.append(list(map(int,input())))
ans = bfs(0,0,N-1,M-1)
print(ans+1)
