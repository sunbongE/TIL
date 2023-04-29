# 1486 장훈이의높은선반
def dfs(n, sm):
    global ans
    if ans <= sm - B:
        return
    if n == N:
        if sm >= B:
            ans = min(ans, sm - B)
        return
    dfs(n + 1, sm + H[n])
    dfs(n + 1, sm)


for case in range(1, 1 + int(input())):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    ans = 1e9
    v = [0] * N
    # 16 - sm 이 가장 작은 것을 구하는 문제
    dfs(0, 0)
    print(f"#{case} {ans}")
