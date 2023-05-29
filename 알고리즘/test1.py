# from pprint import pprint


# def dfs(i, j, temp):
#     global ans
#     # pprint(v)

#     if "".join(temp).count("Y") >= 4:  # 도연파가 4이상이면 안댐
#         return
#     if len(temp) >= 7:
#         # print(temp)
#         if "".join(temp).count("S") >= 4 and len(temp) == 7:  # 도연파가 4명이상이면 답 갱신
#             ans += 1
#             print(temp)
#             # pprint(v)
#         return

#     for di, dj in ((0, 1), (1, 0)):  # 우, 하 순회.
#         ni, nj = i + di, j + dj
#         if 0 <= ni < 5 and 0 <= nj < 5 and not v[ni][nj] and v[i][j] == 1:
#             v[ni][nj] = 1
#             dfs(ni, nj, temp + [arr[ni][nj]])
#             v[ni][nj] = 0
#             # dfs(ni, nj, temp)


# arr = [list(map(str, input())) for _ in range(5)]
# ans = 0
# v = [[0] * 5 for _ in range(5)]
# for i in range(5):
#     for j in range(5):
#         v[i][j] = 1
#         dfs(i, j, [arr[i][j]])
#         pprint(v)
