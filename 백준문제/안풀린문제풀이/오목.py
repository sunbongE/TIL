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
for _ in range(n):
    temp_list = list(map(int,input().split()))
    board.append(temp_list)
#2중 반복문으로 탐색
for y in range(n):
    for x in range(n):

        if board[y][x] == 1 or board[y][x] == 2:
            
            for d in range(4): # 델타 값을 반복해서 넣음
                stone_cnt = 1
                ny = y +dy[d]
                nx = x +dx[d]


pprint(board)