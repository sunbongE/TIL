for case in range(1, int(input()) + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    dp = [0] * (N)
    dp[0] = lst[0]
    for i in range(1, N):
        dp[i] = max(lst[i], dp[i - 1] + lst[i])
    print(max(dp))
