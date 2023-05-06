# # # import sys

# # # input = sys.stdin.readline
# N, K = map(int, input().split())

# li = [list(map(int, input().split())) for _ in range(N)]
# dp = li[0]

# for i in range(1, N):
#     for j in range(K):
#         dp[j] += max(li[i][:j] + li[i][j + 1 :])
# print(max(dp))
# # -------------------------------------
import sys

input = sys.stdin.readline

N, K = map(int, input().split())
satis = [list(map(int, input().split())) for _ in range(N)]


dp = [[0] * K for _ in range(N)]
dp[0] = satis[0]
temp = sorted(dp[0])
info = []

for i in range(1, N):
    tmp = (temp[-1], temp[-2])
    for j in range(K):
        if dp[i - 1][j] == tmp[0]:
            dp[i][j] = satis[i][j] + tmp[1]
        else:
            dp[i][j] = satis[i][j] + tmp[0]
    temp = sorted(dp[i])

print(max(dp[-1]))
