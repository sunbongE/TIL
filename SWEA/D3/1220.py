
import sys
sys.stdin = open('1220.txt')



for _ in range(10):

    M=int(input())
    ans = 0
    arr = [[*map(int,input().split())] for _ in range(M)]
        
    # n, s = 1, 2

    for y in range(M-1):
        cnt = 0
        state=0
        for x in range(M):

            if arr[x][y] != 0:
                state+=1
                
                # cur = arr[x][y]
                # next = arr[x][y+1]
            

    print(cnt)