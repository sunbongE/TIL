n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1
print(max(dp))