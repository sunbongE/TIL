# 햄버거 다이어트..?
# 문제가 아마도 백트레킹?
# 선택을 한다 안 한다 로 재귀호출?
# if n == N : 종료 조건
# ans와 현재 맛의 점수랑 비교를 해야하는데 칼로리랑 비교햇음..
# 맛을 담는 변수를 하나 더 만들어야할듯


def dfs(n, temp, now_kcal):
    global ans
    # 가지치기
    if now_kcal > L:
        return
    # 종료조건
    if n == N:
        ans = max(ans, temp)
        # print(ans, now_kcal)
        return

    dfs(n + 1, temp + info[n][0], now_kcal + info[n][1])  # 선택을 한다.
    dfs(n + 1, temp, now_kcal)  # 선택안한거


# 입력
for case in range(1, int(input()) + 1):
    N, L = map(int, input().split())

    info = [list(map(int, input().split())) for _ in range(N)]
    ans = 0
    now_kcal = 0  # 이 값이 L이하여야한다.

    dfs(0, 0, 0)
    print(f"#{case} {ans}")
