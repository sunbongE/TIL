n = int(input())
t = []
p = []
dp = []

for i in range(n):
    a, b = map(int, input().split())
    t.append(a)
    p.append(b)
    dp.append(b)
dp.append(0)

for i in range(n - 1, -1, -1):
    if t[i] + i > n:  # 전체 일수를 넘어가면 이전 값을 그대로 받아온다.
        dp[i] = dp[i + 1]
    else:  #
        dp[i] = max(dp[i + 1], p[i] + dp[i + t[i]])
print(dp[0])
