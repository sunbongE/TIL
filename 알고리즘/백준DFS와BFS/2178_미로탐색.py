from pprint import pprint

def bfs(si,sj,ei,ej):
    q=[] 
    v = [[0]*M for _ in range(N)] # 방문처리

    q.append((si,sj)) # 시작 좌표를 입력으로 받음
    v[si][sj] = 1 # 처음 시작 위치 방무처리

    while q:
        ci,cj = q.pop(0) # 현재위치를 시작위치로 받음
        if (ci,cj)==(ei,ej):# 현재위치와 끝 위치가 같다면 끝냄
            return v[ei][ej]

        for di,dj in ((-1,0),( 1,0),(0,-1),(0,1)): #상하좌우 
            ni,nj = ci+di, cj+dj
            if 0<=ni<N and 0<=nj<M and arr[ni][nj] == 1 and v[ni][nj] == 0: #바뀔 위치가 조건에 맞으면 
                q.append((ni,nj))   
                v[ni][nj] = v[ci][cj]+1 # 방문처리를 하면서 1을 더해 주는데 이게 최단 거리가 되는거디..

N,M = map(int,input().split())
arr = [list(map(int,input())) for _ in range(N)]

ans = bfs(0,0,N-1,M-1)
print(ans)