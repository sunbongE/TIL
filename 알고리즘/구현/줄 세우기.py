import sys

input = sys.stdin.readline

n = int(input())

dp = [0 for _ in range(n + 1)]
for i in list(map(int, input().split())):
    dp[i] = dp[i - 1] + 1
    print(dp)
print(n - max(dp))
