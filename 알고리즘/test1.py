# import sys

# input = sys.stdin.readline
# target = input().strip()
# word = input().strip()
# L1 = len(target)
# L2 = len(word)

# dogam = dict()

# for i in range(0, L1 - L2 + 1):
#     dogam[target[i : i + L2]] = 1

# ans = dogam.get(word, 0)
# print(ans)

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]
dp = [0] * (k + 1)
dp[0] = 1
for coin in coins:
    for i in range(coin, k + 1):
        dp[i] += dp[i - coin]
print(dp[k])
