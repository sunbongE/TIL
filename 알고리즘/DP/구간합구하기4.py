import sys

input = sys.stdin.readline
n, m = map(int, input().split())

nums = list(map(int, input().split()))
dp = [0] * (n + 1)

for i in range(1, 1 + n):
    dp[i] = dp[i - 1] + nums[i - 1]

for i in range(m):
    start, end = map(int, input().split())

    print(dp[end] - dp[start - 1])
