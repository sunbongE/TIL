 
from array import array
import sys
sys.stdin = open('t.txt','r')
from pprint import pprint
# 문제 분석 2중 리스트를 이용하는 문제인건 확실함
# 델타 탐색을 해야함 시계방향으로 우 하 좌 상
# 범위 지정하고 값이 0이 아니면 이동 
# 그렇지 않다면 다음 방향으로 탐색 
#  #
delta_x = [0,1,0,-1]
delta_y = [1,0,-1,0]
for t in range(int(input())):
   
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    # pprint(mat)
    col, row = 0,0
    v = 0
    arr[col][row] = 1
    dcol = [-1,0,1,0]
    drow = [0,1,0,-1]

    for i in range(1,N*N+1):# 델타 탐색 
        arr[col][row] = i
        col += dcol[v]
        row += drow[v]

        if col < 0 or row < 0 or N <= col or N <= row or arr[col][row] != 0:
            col -= dcol[v]
            row -= drow[v]

            v = (v+1) % 4 
            col = col + dcol[v]
            row += drow[v]
    print(f'#{t+1}')
    for i in arr:
        for j in i:
            print(j,end=' ')
        print()