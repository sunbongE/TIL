# def dfs(n, sm):
#     global ans
#     # 가지치기.
#     if sm >= ans:
#         return
#     # 12달을 모두 돌았을 때 가격
#     if n > 12:
#         ans = min(ans, sm)
#         return

#     dfs(n + 1, sm + (plan[n] * day))
#     dfs(n + 1, sm + mon)
#     dfs(n + 3, sm + mon3)
#     dfs(n + 12, sm + year)


# for case in range(1, int(input()) + 1):
#     day, mon, mon3, year = map(int, input().split())
#     # 0~12까지 생성
#     plan = [0] + list(map(int, input().split()))
#     ans = 1e9
#     # 종료조건 횟수, 비용 합계를 넘겨준다.
#     dfs(0, 0)
#     print(f"#{case} {ans}")

# dp 풀이
for case in range(1, int(input()) + 1):
    day, mon, mon3, year = map(int, input().split())
    # 0~12까지 생성
    plan = [0] + list(map(int, input().split()))
    # ans = 1e9
    dp = [0] * 13

    # 1~12까지 for문을 통해 순회하면 각 월에대한 최소 값을 구한다.
    for i in range(1, 13):
        mn = dp[i - 1] + plan[i] * day  # 1일권
        mn = min(mn, dp[i - 1] + mon)  # 1달권
        if i >= 3:
            mn = min(mn, dp[i - 3] + mon3)
        if i >= 12:
            mn = min(mn, dp[i - 12] + year)
        dp[i] = mn
    ans = dp[12]
    print(dp)
    print(f"#{case} {ans}")
