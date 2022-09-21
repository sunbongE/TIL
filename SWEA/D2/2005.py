import sys 
sys.stdin = open('2005.txt','r')
from pprint import pp, pprint
# 0~N+1 까지 arr만듬
# 델타 탐색 느낌으로 왼쪽 위, 위에 있는 수를 더한 값을 현재 값에 넣음
# #
for case in range(int(input())):
    n = int(input())
    arr = [[0]*(n+1) for _ in range(n+1)]
    arr[1][1] = 1
    
    for y in range(2,n+1):
        for x in range(1,y+1):
            # pass
            arr[y][x] = arr[y-1][x-1] + arr[y-1][x]

    print(f'#{case+1}')
    for i in range(1,n+1):
        for j in range(1,i+1):
            print(arr[i][j],end=' ')
        print()


