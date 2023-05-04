# 전기버스2
def dfs(n, cnt, sm):
    global ans
    if cnt >= ans:
        return
    if n == N - 1:
        ans = min(ans, cnt)
        return

    # 유망한 답은 교체를 최대한 안하고 가는 것이니까
    # 교체를 안하는 것을 먼저 호출한다.
    #
    if sm > 0:  # 배터리 잔량이 남아있다면 교체를 안할 수 있다.
        dfs(n + 1, cnt, sm - 1)
    # 넘겨줄때는 배터리 -1 해야함.
    dfs(n + 1, cnt + 1, stations[n] - 1)


for case in range(1, 1 + int(input())):
    inp = list(map(int, input().split()))
    N = inp[0]
    stations = inp[1:]
    ans = N  # 무조건 갱신되게 성정.
    # print(stations)
    # 첫번째 베터리는 교체한거로안침
    # (n,교체수, 배터리잔량)
    dfs(1, 0, stations[0] - 1)
    print(f"#{case} {ans}")
