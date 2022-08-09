import sys
sys.stdin = open('','r')

dy = [0,1,-1,1]
dx = [1,0,1,1]
black = 1
white = 2
n=19
board = []
for _ in range(n):
    temp_list = list(map(int,input().split()))
    board.append(temp_list)

