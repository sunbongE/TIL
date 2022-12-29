# from pprint import pprint
# from collections import deque

# def bfs(arr,x,y):

#     queue=deque()
#     queue.append((x,y))
#     arr[x][y]=0 # 탐색한 곳은 0으로 변경
#     cnt = 1

#     while queue:
#         x,y = queue.popleft()

#         for dx,dy in ((-1,0),(1,0),(0,-1),(0,1)): #상하좌우
#             nx,ny = x+dx, y+dy
#             #범위설정
#             if 0<=nx<N and 0<=ny<N and arr[nx][ny]==1:
#                 arr[nx][ny] = 0
#                 queue.append((nx,ny))
#                 cnt += 1
#     return cnt

# N = int(input())
# arr = [list(map(int, input())) for _ in range(N)]


# count=[]

# for i in range(N) : # 첫번째 시작하는 좌표를 찾아서 보낸것이다.

#     for j in range(N):
#          if arr[i][j] == 1:
#             count.append(bfs(arr, i, j)) # 리턴값을 count변수에 담을거임

# count.sort()    
# print(len(count))

# for i in range(len(count)):
#     print(count[i])



N = int(input())
graph = [list(map(int, input())) for _ in range(N)]
num = []
# 상하좌우
dx = [-1,1,0,0] 
dy = [0,0,-1,1]

def DFS(x,y):
    if x<0 or x>=N or y<0 or y >=N: # x,y의 위치가 범위 밖이면 False를 리턴한다. 
        return False
    
    if graph[x][y] == 1: # 그래프에서 1이면 
        global count # 단지 수를 기록한다.
        count += 1
        graph[x][y] = 0 # 재방문을 막기위해 0으로 바꿔준다.
        for i in range(4): # 4방향 탐색
            nx = x +dx[i]
            ny = y +dy[i]
            DFS(nx,ny)
        return True
    return False
    

count = 0
result = 0

for i in range(N):
    for j in range(N): 
        if DFS(i,j) == True:
            # 처음 시작하는 위치를 찾아서 함수 호출
            num.append(count) # 함수가 끝나고 기록된 단지수를 num에 저장
            result += 1 # 촌수를 기록한다.
            count = 0 # count는 다시 0으로 해줘야 다음 단지수를 기록할수 있다.
        
num.sort() 
# 단지수를 오름차순 정렬한다.
print(result) # 촌수를 먼저 출력한다.
for i in range(len(num)): # 정렬된 단지수를 출력한다.
	print(num[i])