n, k = map(int, input().split())
moneys = set()
for _ in range(n):
    moneys.add(int(input()))
INF = k + 1
dp = [INF] * (k + 1)
dp[0] = 0
for money in moneys:
    for i in range(1, k + 1):
        if i - money >= 0:
            dp[i] = min(dp[i - money] + 1, dp[i])
if dp[k] != INF:
    print(dp[k])
else:
    print(-1)
