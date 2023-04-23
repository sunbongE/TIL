n = int(input())

nums = list(map(int, input().split()))

dp = [1] * n

for i in range(n - 1, -1, -1):
    for j in range(n - i):
        print(i, n - 1 - j)
        if i != n - 1 - j:
            if nums[i] > nums[n - 1 - j]:
                dp[i] = max(dp[i], dp[n - 1 - j] + 1)
print(dp)
print(max(dp))
