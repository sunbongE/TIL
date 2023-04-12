T = int(input())
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for _ in range(T):
    N = int(input())
    arr = [[0] * N for __ in range(N)]
    x, y, di = 0, 0, 0
    arr[x][y] = 1
    while arr[x][y] != N**2:
        nx, ny = x + dx[di], y + dy[di]
        if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == 0:
            arr[nx][ny] = arr[x][y] + 1
            x, y = nx, ny
        else:
            di = (di + 1) % 4
    print(f"#{_+1}")
    for ar in arr:
        print(*ar)
