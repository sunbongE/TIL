from pprint import pprint
from collections import deque

def bfs(arr,x,y):

    queue=deque()
    queue.append((x,y))
    arr[x][y]=0 # 탐색한 곳은 0으로 변경
    cnt = 1

    while queue:
        x,y = queue.popleft()

        for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)): #상하좌우
            nx,ny = x+dx, y+dy
            #범위설정
            if 0<=nx<N and 0<=ny<N and arr[nx][ny]==1:
                arr[nx][ny] = 0
                queue.append((nx,ny))
                cnt += 1
    return cnt

N = int(input())
arr = [list(map(int, input())) for _ in range(N)]


count=[]

for i in range(N) : # 첫번째 시작하는 좌표를 찾아서 보낸것이다.

    for j in range(N):
         if arr[i][j] == 1:
            count.append(bfs(arr, i, j)) # 리턴값을 count변수에 담을거임

count.sort()    
print(len(count))

for i in range(len(count)):
    print(count[i])