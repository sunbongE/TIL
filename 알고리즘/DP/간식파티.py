import sys

input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
dp = [0] * N
dp[0] = nums[0]

for i in range(N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j] + nums[i])
        else:
            dp[i] = max(dp[i], nums[i])
print(max(dp))
