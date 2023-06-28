for case in range(1, 1 + int(input())):
    ans = 0  # 답

    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # + 자 방향
    dx = (-1, 1, 0, 0)
    dy = (0, 0, -1, 1)
    # x자 방향
    ddx = (-1, -1, 1, 1)
    ddy = (-1, 1, -1, 1)

    for i in range(N):
        for j in range(N):
            temp = arr[i][j]
            # + 모양
            for idx in range(4):
                ci, cj = i, j  # 현재 위치
                for cnt in range(M - 1):  # M-1번 반복
                    ni, nj = ci + dx[idx], cj + dy[idx]  # 방향으로 이동.
                    if 0 <= ni < N and 0 <= nj < N:  # 범위 내에 있으면 값 더하기.
                        temp += arr[ni][nj]
                        ci, cj = ni, nj  # 현재 위치도 갱신.
                    else:  # 없으면 인덱스 바꾸기.
                        break
            ans = max(ans, temp)
            temp = arr[i][j]
            # x모양
            for idx in range(4):
                ci, cj = i, j
                for cnt in range(M - 1):  # M-1번 반복
                    ni, nj = ci + ddx[idx], cj + ddy[idx]  # 방향으로 이동.
                    if 0 <= ni < N and 0 <= nj < N:  # 범위 내에 있으면 값 더하기.
                        temp += arr[ni][nj]
                        ci, cj = ni, nj  # 현재 위치도 갱신.
                    else:  # 없으면 인덱스 바꾸기.
                        break

            ans = max(ans, temp)
    print(f"#{case} {ans}")
