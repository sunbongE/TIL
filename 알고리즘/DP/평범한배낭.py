# dp
from pprint import pprint

N, K = map(int, input().split())

# 각 물건의 무게와 가치를 입력받는다.
items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

# dp[i][j]는 배낭의 용량이 j일 때, i번째 물건까지 고려했을 때 최대 가치이다.
dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):  # 각 아이템을 돌면서 그 아이템의 무게와 j 무게를 비교한다.
    for j in range(1, K + 1):
        W, V = items[i - 1]
        # print(items)
        # print(W, V, "?")
        # pprint(dp)
        if W > j:  # 내 무게가 초과되면 전에 값 상속받기
            dp[i][j] = dp[i - 1][j]
        else:  # j - W => 현재 찾는 무게 - 내 무게 + 내 가치
            # ==> 이 식은 만약 무게 3이고 찾는 무게 4라면 4-3 해서 1에있는 가치에 내 가치를 더하는 것이다.
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W] + V)
# print(dp)
print(dp[N][K])

# -------------code_only-----------------------
N, K = map(int, input().split())

items = []
for _ in range(N):
    W, V = map(int, input().split())
    items.append((W, V))

dp = [[0] * (K + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, K + 1):
        W, V = items[i - 1]

        if W > j:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - W] + V)
print(dp[N][K])
