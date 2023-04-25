for case in range(1, int(input()) + 1):
    n = int(input())

    dp = [[1, 0, 0] for _ in range(n + 1)]
    # 1은 계속 1이고 2는 '현재 수' - '2' + 1
    # 3은 '현재수' - 3 의 sum
    # print(dp)
    for i in range(2, n + 1):
        dp[i][1] = dp[i - 2][1] + 1
        if i - 3 >= 0:
            dp[i][2] = sum(dp[i - 3])
            # print(i, dp[i - 3])
    print(sum(dp[n]))
    # print(dp)
