import sys
sys.stdin = open("1216.txt")
from pprint import pprint

for _ in range(10):
    case = int(input())
    leng=1
    palindrome = []
    arr = [list(input()) for _ in range(100)]
    arr2 = [[0]*100 for _ in range(100)]
    for i in range(100):
        for j in range(100):
            arr2[j][i]=arr[i][j] # arr의 전치 행렬
    ans = 1

    m=0
    e = 99
    for y in range(100):
        for x in range(100):
            # # print(m)
            # print(arr[y+x][y:100-x])
            # print(arr[y+x][m], arr[y+x][-1-x])
            for a in range(100):
                if arr[a][m] == arr[a][-1-x]:

                    if arr[a][m:100-x] == arr[a][m:100-x][::-1] and ans < len(arr[a][m:100-x]):
                        ans = len(arr[a][m:100-x])
                if ans > len(arr[a][x:e+1]):
                    break
                if arr[a][e] == arr[a][x]: # 뒤 고정
                    if arr[a][x:e+1] == arr[a][x:e+1][::-1] and ans < len(arr[a][x:e+1]):
                        ans = len(arr[a][x:e+1])

                if ans > len(arr[a][y:100-x]):
                    break
                # print(arr[a][y:100-x])
            # print(arr[y][e],arr[y][x])
        m+=1 
        e-=1        
                
    m=0
    e = 99
    for y in range(100):
        for x in range(100):
            # # print(m)
            # print(arr[y+x][y:100-x])
            # print(arr[y+x][m], arr[y+x][-1-x])
            for a in range(100):
                if arr2[a][m] == arr2[a][-1-x]:

                    if arr2[a][m:100-x] == arr2[a][m:100-x][::-1] and ans < len(arr2[a][m:100-x]):
                        ans = len(arr2[a][m:100-x])
                if ans > len(arr[a][x:e+1]):
                    break
                if arr2[a][e] == arr2[a][x]: # 뒤 고정
                    if arr2[a][x:e+1] == arr2[a][x:e+1][::-1] and ans < len(arr2[a][x:e+1]):
                        ans = len(arr2[a][x:e+1])

                if ans > len(arr2[a][y:100-x]) :
                    break
                # print(arr2[a][y:100-x])
            # print(arr[y][e],arr[y][x])
        m+=1 
        e-=1        
    print(f'#{case} {ans}')