from pprint import pprint

t = int(input())
for case in range(1, 1 + t):
    N = int(input())

    arr = [[0] * N for _ in range(N)]
    # 우, 하, 좌 , 상
    di = (0, 1, 0, -1)
    dj = (1, 0, -1, 0)
    dr_idx = 0

    si, sj = 0, 0
    arr[si][sj] = 1
    while arr[si][sj] != N * N:
        # print(temp)
        ni, nj = si + di[dr_idx], sj + dj[dr_idx]
        # 범위내, arr가 0이면
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            arr[ni][nj] += arr[si][sj] + 1
            si, sj = ni, nj

        # 벽 만난 경우 방향을 바꿔야합니다.
        #
        else:
            dr_idx = (dr_idx + 1) % 4

    print(f"#{case}")
    for ans in arr:
        print(*ans)
