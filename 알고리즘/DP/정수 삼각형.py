# import sys

# input = sys.stdin.readline
# n = int(input())
# triangle = []
# for _ in range(n):
#     triangle.append(list(map(int, input().split())))
# if n > 1:
#     triangle[1][0] = triangle[1][0] + triangle[0][0]
#     triangle[1][1] = triangle[1][1] + triangle[0][0]
#     for i in range(1, n - 1):
#         for j in range(len(triangle[i + 1])):

#             if j == 0:  # 인덱스 0이면 이전 높이에서 0이랑 더한값
#                 triangle[i + 1][j] = triangle[i + 1][j] + triangle[i][j]
#             elif j == len(triangle[i + 1]) - 1:  # 마지막은 이전의 마지막이랑 더한값
#                 triangle[i + 1][j] = triangle[i + 1][j] + triangle[i][j - 1]
#             else:
#                 triangle[i + 1][j] = max(
#                     triangle[i + 1][j] + triangle[i][j],
#                     triangle[i + 1][j] + triangle[i][j - 1],
#                 )
#     print(max(triangle[-1]))
# else:
#     print(*max(triangle))


n = int(input())

dt = [0] * (n + 1)

for idx in range(n):
    arr = list(map(int, input().split()))
    temp = list(dt)

    for j in range(1, len(arr) + 1):
        dt[j] = max(temp[j - 1] + arr[j - 1], temp[j] + arr[j - 1])

print(max(dt))
