T = int(input())

for case in range(1, 1 + T):
    N, K = map(int, input().split())
    dp = [0] * (K + 1)

    for _ in range(N):
        V, C = map(int, input().split())
        if V > K:
            continue
        for i in range(K, 0, -1):
            if i + V <= K:
                dp[i + V] = max(dp[i + V], dp[i] + C)
        dp[V] = max(dp[V], C)
        # print(dp)
    print("#{} {}".format(case, max(dp)))

# 풀이 설명
# dp[i + V] => 이건 지금 순회하는 무게에 내 무게를 더한 값을 갱신하는 것이고
# 순회를 역순으로 함으로 큰 수부터 갱신하면 좋다함 뭔지모름
#
