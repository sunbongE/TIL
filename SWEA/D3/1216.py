import sys
sys.stdin = open("1216.txt")
from pprint import pprint

for _ in range(10):
    case = int(input())
    arr = [list(input()) for _ in range(100)]
    arr2 = [[0]*100 for _ in range(100)]

    for i in range(100):
        for j in range(100):
            arr2[j][i]=arr[i][j] # arr의 전치 행렬

    leng=1

    e = 99
    for y in range(100):
        for x in range(100):

            for a in range(100):
                # if leng > len(arr[a][x:e+1]):
                #     break
                if leng > len(arr[a][y:100-x]):
                    break

                if arr[a][x] == arr[a][-1-x]:
                    # 0,1,2/0

                    if arr[a][x:100-x] == arr[a][x:100-x][::-1] and leng < len(arr[a][x:100-x]): #앞자리와 뒤자리가 같은 글이면
                        leng = len(arr[a][x:100-x])
                        
                

                if arr[a][e] == arr[a][x]: # 뒤 고정
                    # 0,1,2/99     0,1,2 / 0
                    if arr[a][x:e+1] == arr[a][x:e+1][::-1] and leng < len(arr[a][x:e+1]):
                        leng = len(arr[a][x:e+1])

                
                # print(arr[a][y:100-x])
            # print(arr[y][e],arr[y][x])
        e-=1        
                
    e = 99
    for y in range(100):
        for x in range(100):
            # # print(m)
            # print(arr[y+x][y:100-x])
            # print(arr[y+x][m], arr[y+x][-1-x])
            for a in range(100):

                if leng > len(arr[a][x:e+1]):
                    break
                if leng > len(arr2[a][y:100-x]):
                    break

                if arr2[a][x] == arr2[a][-1-x]:

                    if arr2[a][x:100-x] == arr2[a][x:100-x][::-1] and leng < len(arr2[a][x:100-x]):
                        leng = len(arr2[a][x:100-x])
                
                if arr2[a][e] == arr2[a][x]: # 뒤 고정
                    if arr2[a][x:e+1] == arr2[a][x:e+1][::-1] and leng < len(arr2[a][x:e+1]):
                        leng = len(arr2[a][x:e+1])

                
                # print(arr2[a][y:100-x])
            # print(arr[y][e],arr[y][x])
        e-=1        
    print(f'#{case} {leng}')



#     for tc in range(10):
#   N = int(input())
#   characters = [list(input()) for _ in range(100)]
#   characters2 = list(map(list, zip(*characters)))
#   cnt = 100
#   found = False

#   while cnt <= 100:
#     for i in range(100-cnt+1):
#       for j in range(100-cnt+1):
#         if characters[i][j:j+cnt] == characters[i][j:j+cnt][::-1]:
#           found = True
#         if characters2[i][j:j+cnt] == characters2[i][j:j+cnt][::-1]:
#           found = True
#     if found == True:
#       break
#     cnt -= 1
#   print(f"#{N} {cnt}")