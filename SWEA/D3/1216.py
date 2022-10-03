import sys
sys.stdin = open("1216.txt")
from pprint import pprint
 # 내 풀이 
for _ in range(10):
    case = int(input())
    arr = [list(input()) for _ in range(100)]
    arr2 = [[0]*100 for _ in range(100)]

    for i in range(100):
        for j in range(100):
            arr2[j][i]=arr[i][j] # arr의 전치 행렬

    leng=1

    for y in range(100):
        for x in range(100):
            for a in range(100):
                
                if leng > len(arr[a][y:100-x]):
                    break
                if arr[a][x] == arr[a][-1-x]:
                    # 0,1,2/0
                    if arr[a][x:100-x] == arr[a][x:100-x][::-1] and leng < len(arr[a][x:100-x]): #앞자리와 뒤자리가 같은 글이면
                        leng = len(arr[a][x:100-x])
                        break
                if arr[a][100-y-1] == arr[a][x]: # 뒤 고정
                    # 0,1,2/99     0,1,2 / 0
                    if arr[a][x:100-y] == arr[a][x:100-y][::-1] and leng < len(arr[a][x:100-y]):
                        leng = len(arr[a][x:100-y])
                        break
                # print(e,100-y-1)
    for y in range(100):
        for x in range(100):

            for a in range(100):

             
                if leng > len(arr2[a][y:100-x]):
                    break

                if arr2[a][x] == arr2[a][-1-x]:

                    if arr2[a][x:100-x] == arr2[a][x:100-x][::-1] and leng < len(arr2[a][x:100-x]):
                        leng = len(arr2[a][x:100-x])
                        break
                if arr2[a][100-y-1] == arr2[a][x]: # 뒤 고정
                    if arr2[a][x:100-y] == arr2[a][x:100-y][::-1] and leng < len(arr2[a][x:100-y]):
                        leng = len(arr2[a][x:100-y])
                        break

                
                # print(arr2[a][y:100-x])
            # print(arr[y][e],arr[y][x])
    print(f'#{case} {leng}')


# 모르는 풀이

# for tc in range(10):
#   N = int(input())
#   characters = [list(input()) for _ in range(100)] # 배열 입력받음
#   characters2 = list(map(list, zip(*characters))) # 전치 행렬을 만들었음
#   cnt = 100
#   found = False

#   while cnt <= 100:
#     for i in range(100-cnt+1): # i 0 1 2 3 ...
#       for j in range(100-cnt+1): # 0 1 2 3 ....
#         # print(characters[i][j:j+cnt])
#         if characters[i][j:j+cnt] == characters[i][j:j+cnt][::-1]:
#           found = True
#           # print(characters[i][j:j+cnt])
#         if characters2[i][j:j+cnt] == characters2[i][j:j+cnt][::-1]:
#           found = True
#           # print(characters[i][j:j+cnt])
#     if found == True:
#       break
#     cnt -= 1
#   print(f"#{N} {cnt}")

# 현중님 풀이

# for test_case in range(10):
#     n = int(input())
#     graph = [[i for i in input().strip()] for _ in range(100)]
#     graph_col = [[0]*100 for _ in range(100)]
#     for i in range(100):
#         for j in range(100):
#             graph_col[i][j] = graph[j][i]
#     result = 1
#     flag = True
#     for i in range(100,0,-1): # 100 99 9100 ...
#         if not flag:
#             break
#         for grap in graph:
#             if not flag:
#                 break
#             for j in range(100-i+1): # 0 1 2 3 ...
#                 # print(j,i,j+i)

#                 x = grap[j:j+i]
#                 if x == x[::-1]:
#                     result = max(result, i)
#                     flag = False
#                     break
#     flag = True
#     for i in range(100,0,-1):
#         if not flag:
#             break
#         for grap in graph_col:
#             if not flag:
#                 break
#             for j in range(100-i+1):
#                 # print(j,i,j+i)
#                 x = grap[j:j+i]
#                 # print(x)
#                 if x == x[::-1]:
#                     result = max(result, i)
#                     flag = False
#                     break
#     print(f'#{test_case+1} {result}')