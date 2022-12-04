import sys  
sys.stdin = open("미로1.txt")

def bfs(si,sj):
    q=[]
    v=[[0]*N for _ in range(N)]

    # q에 초기 데이터 삽입, v표시
    q.append((si,sj))   
    #도착여부,,
    v[si][sj]=1             

    while q:
        ci,cj = q.pop(0)
        if arr[ci][cj] == 3:
            return v[ci][cj]

        #네방향 방문    상 하 좌 우
        for di,dj  in ((-1,0),(1,0),(0,-1),(0,1)):
            ni,nj = ci+di, cj+dj
            # 범위안에 있고, 방문을 안했고, 벽이 아니면
            if 0<=ni<N and 0<=nj<N and v[ni][nj]==0 and arr[ni][nj] != 1:
                q.append((ni,nj))
                v[ni][nj]=1 
    return 0

T = 10
for test_case in range(1,T+1):
    case=input()
    N=16    
    arr = [list(map(int,input())) for _ in range(N)] # 배열입력
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2: # 시작위치 찾음
                si,sj = i,j
    ans = bfs(si,sj)
    print(f'#{test_case} {ans}')