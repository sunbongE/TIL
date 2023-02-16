N = int(input())
dp = [[0] * 10 for _ in range(N + 1)]
for i in range(1, 10):
    dp[1][i] = 1  # 자리수 1일때 처리해준거

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]
        elif j == 9:
            dp[i][j] = dp[i - 1][8]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]

print(sum(dp[N]) % 1_000_000_000)
# print(dp)
# 0앞에 올 수 있는 수는 1뿐이고 1앞에 올수 있는 수는 2뿐이고
# 2~8까지는 2개씩
# 9 앞에 올수 있는 수는 8뿐이다.
