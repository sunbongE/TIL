
import sys
sys.stdin = open('1220.txt')
from pprint import pprint
# 1 다음에 오는 2가 있으면 셀 수 있어야 하지만#
# 반복적인 2를 보았을 때 1개로 셀 수 있어야함


for _ in range(10):

    M=int(input())
    ans = 0
    arr = [[*map(int,input().split())] for _ in range(M)]
    # n, s = 1, 2
    cnt = 0
    for y in range(M):
        state = 0

        for x in range(M):

            if state == 0 and arr[x][y] == 1:
                state = 1

            elif state == 1 and arr[x][y] == 2:
                state = 2
                cnt += 1 
                arr[x][y] = 9
            elif state == 2 and arr[x][y] == 1:
                state = 1
    
    print(f'#{_+1} {cnt}')