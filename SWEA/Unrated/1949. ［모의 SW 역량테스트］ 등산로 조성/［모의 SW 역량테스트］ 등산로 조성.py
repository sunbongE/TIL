def dfs(x, y, c):
    global maxLen
    maxLen = max(maxLen, v[x][y])

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if not (0 <= nx < N and 0 <= ny < N) or v[nx][ny]:
            continue

        # 현재 값보다 작다면 이동..
        if arr[nx][ny] < arr[x][y]:
            v[nx][ny] = v[x][y] + 1
            dfs(nx, ny, c)
            v[nx][ny] = 0
        elif c and arr[nx][ny] - K < arr[x][y]: # 공사하고 나보다 작아지는 값이면 공사.
            tmp = arr[nx][ny]
            v[nx][ny] = v[x][y] + 1
            arr[nx][ny] = arr[x][y] - 1
            dfs(nx, ny, c - 1)
            v[nx][ny] = 0
            arr[nx][ny] = tmp


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 공사할 수 있는지 여부 딱 1번 최대 K깊이 만큼 할수있다.
    flag = True
    tVal = 0
    for i in range(N):
        tmp = max(arr[i])
        tVal = max(tmp, tVal)

    # 봉우리의 위치를 찾아 기록.
    target = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == tVal:
                target.append([i, j])

    #  이제 dfs으로 백트 각나옴.
    maxLen = 0
    v = [[0] * N for _ in range(N)]
    for i in range(len(target)):
        x = target[i][0]
        y = target[i][1]
        v[x][y] = 1
        dfs(x, y, 1)
        v[x][y] = 0
    print(f"#{tc} {maxLen}")
