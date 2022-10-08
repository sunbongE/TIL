import sys
sys.stdin = open('1954.txt','r')
from pprint import pprint
# 문제 분석 2중 리스트를 이용하는 문제인건 확실함
# 델타 탐색을 해야함 시계방향으로 우 하 좌 상
# 범위 지정하고 값이 0이 아니면 이동 
# 그렇지 않다면 다음 방향으로 탐색 
#  #

dx =[1, 0, -1, 0]
dy =[0, 1, 0, -1]

for _ in range(int(input())):
    N = int(input())
    arr= [[0]*N for _ in range(N)]
    D = 0
    x, y = 0, 0
    cnt = 1
    arr[y][x] = cnt
    while cnt != N*N:
        nx = x + dx[D]
        ny = y + dy[D]
        if 0 <= nx < N and 0 <= ny < N and arr[ny][nx] == 0:
            x, y = nx, ny 
            cnt += 1
            arr[y][x] = cnt
        else:
            D = (D + 1) % 4
    print('#',_+1,sep='')
    for lst in arr:
        print(*lst)

