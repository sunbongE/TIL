# 4가지의 모든 방법을 다 해보는 백트레킹 방법으로 접근한다.
# def dfs(n, pay):
#     global ans
#     if pay >= ans:
#         return
#     if n > 12:
#         ans = min(ans, pay)
#         return

#     dfs(n + 1, pay + (day * plan[n]))
#     dfs(n + 1, pay + mon)
#     dfs(n + 3, pay + mon3)
#     dfs(n + 12, pay + year)


# for case in range(1, 1 + int(input())):
#     day, mon, mon3, year = map(int, input().split())

#     plan = [0] + list(map(int, input().split()))
#     # print(plan)
#     ans = 365 * 3000

#     dfs(1, 0)
#     print(f'#{case} {ans}')

# 그리디한 방법 dp
# 각 월을 돌면서 계산할 수 있는 비용들을 전부 계산하고 최소값을 갱신하는 것이
# 답인데
#

for case in range(1, 1 + int(input())):
    day, mon, mon3, year = map(int, input().split())

    plan = [0] + list(map(int, input().split()))
    # print(plan)
    ans = 365 * 3000
    d = [0] * 13
    for i in range(1, 13):
        mn = d[i - 1] + plan[i] * day  # 일일권 구매
        mn = min(mn, d[i - 1] + mon)  # 월간 이용권 구매
        if i >= 3:  # 3개월 이용권 구매
            mn = min(mn, d[i - 3] + mon3)
        if i >= 12:  # 1년 이용권 구매
            mn = min(mn, d[i - 12] + year)
        d[i] = mn  # 위 과정을 통해 걸러진 최소값을 기록한다.

    print(f"#{case} {d[12]}")
