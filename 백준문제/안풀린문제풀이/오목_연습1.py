import sys
sys.stdin = open('오목.txt','r')
from pprint import pprint

#
dy = [0,1,-1,1]
dx = [1,0,1,1]
black = 1
white = 2
n=19
board = []
win = 0

for _ in range(n):
    temp_list = list(map(int,input().split()))
    board.append(temp_list)
# print(board)
#2중 반복문으로 탐색
for y in range(n): # 열 우선 , 왼쪽 좌표값을 알아야해서.
    for x in range(n):

        if board[y][x] == 1 or board[y][x] == 2: # 검은 돌이나 흰 돌이면 참
            
            for d in range(4): # 델타 값을 반복해서 넣음
                stone_cnt = 1

                ny = y +dy[d]
                nx = x +dx[d]
                
                while 1:

                    if not (-1< ny < n and -1 < nx < n):
                        break
                    if board[y][x] != board[ny][nx]:
                        break

                    stone_cnt += 1

                    ny = ny + dy[d]
                    nx = nx + dx[d]
                    # 다음 돌까지 탐색할 수 있게 구현했다.
                # while 돌다가 if에 막혀서 빠져나왔을 때
                #돌이 5개라면 실행
                if stone_cnt == 5:  
                    #이전 좌표 구하는거
                    prev_x = x - dx[d]
                    prev_y = y - dy[d]
                    # 이전 값이 범위에 있어야하고 현재 돌과 달라야함
                    if not (-1<prev_x<n and -1<prev_y<n) or board[y][x] != board[prev_y][prev_x]:
                        win = board[y][x]
                        print(win)
                        print(y+1,x+1)
if win == 0:
    print(win)

                    

# pprint(board)