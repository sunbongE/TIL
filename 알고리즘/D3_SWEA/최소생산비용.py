# 최소 생산 비용
# 가능한 모든 경우를 구하면서
# 최소 비용을 갱신한다.
def dfs(n, sm):
    global min_val
    # 가지치기.
    if sm >= min_val:
        return
    # 종료조건
    if n == N:
        min_val = min(min_val, sm)
        return

    for i in range(N):
        if v[i] == 0:
            v[i] = 1
            dfs(n + 1, sm + arr[n][i])
            v[i] = 0


for case in range(1, 1 + int(input())):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 한 곳에 하나니까 중복 선택을 못하게 해야함.
    v = [0] * N  # 제품 선택 여부 기록
    min_val = float("inf")
    dfs(0, 0)
    print(f"#{case} {min_val}")
