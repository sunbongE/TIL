# import sys
# sys.stdin = open("t.txt")
# from pprint import pprint






# for _ in range(1):
#     tc = int(input())
    
#     result = 1

#     #가로줄 확인
#     Garo_lst = []
#     for i in range(8):
#         Data = input()
#         Garo_lst.append(Data)
#         #회문 길이
#         for M in range(8, result, -1):
#             if result > M:
#                 break

#             for k in range(8-M+1):
#                 print(Data[k:M+k],k,M,M+k)
#                 if Data[k:M+k] == Data[k:M+k][::-1]:
#                     if len(Data[k:M+k]) > result:
#                         result = len(Data[k:M+k])
#                         # print(Data[k:M+k], k,M)


#     #세로줄 확인
#     Sero_lst = []
#     Sero_sub_lst = ''
#     for x in range(8):
#         for y in Garo_lst:
#             Sero_sub_lst += y[x]
#         Sero_lst.append(Sero_sub_lst)
#         Sero_sub_lst =''

#     for sero_data in Sero_lst:
#         for M in range(8, result, -1):
#             if result > M:
#                 break
#             for k in range(8-M+1):
#                 if sero_data[k:M+k] == sero_data[k:M+k][::-1]:
#                     if len(sero_data[k:M+k]) > result:
#                         result = len(sero_data[k:M+k])
#                         print(sero_data[k:M+k], k,M)

#     print("#%d %s"%(tc, result))


#     # --------- 공주님 풀이
for test_case in range(1):
    n = int(input())
    graph = [[i for i in input().strip()] for _ in range(8)]
    graph_col = [[0]*8 for _ in range(8)]
    for i in range(8):
        for j in range(8):
            graph_col[i][j] = graph[j][i]
    result = 1
    flag = True
    for i in range(8,0,-1): # 8 99 98 ...
        if not flag:
            break
        for grap in graph:
            if not flag:
                break
            for j in range(8-i+1): # 0 1 2 3 ...
                # print(j,i,j+i)

                x = grap[j:j+i]
                # print(x)
                

                if x == x[::-1]:
                    result = max(result, i)
                    flag = False
                    break
    flag = True
    for i in range(8,0,-1):
        if not flag:
            break
        for grap in graph_col:
            if not flag:
                break
            for j in range(8-i+1):
                print(j,i,j+i)
                x = grap[j:j+i]
                print(x)
                if x == x[::-1]:
                    result = max(result, i)
                    flag = False
                    break
    print(f'#{test_case} {result}')