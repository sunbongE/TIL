N = int(input())

dp = [[0] * 12 for _ in range(N + 1)]
dp[1][2:11] = [1] * 9
for i in range(2, N + 1):
    for j in range(1, 11):
        dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]
ans = sum(dp[N])
print(ans % 1000000000)
