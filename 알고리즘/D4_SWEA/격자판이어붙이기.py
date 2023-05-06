def dfs(sx, sy, val):
    global result
    if len(val) == 7:
        result.append(val)
        return

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = sx + dx, sy + dy
        if 0 <= nx < 4 and 0 <= ny < 4:
            dfs(nx, ny, val + str(arr[nx][ny]))


for case in range(1, 1 + int(input())):
    arr = [list(map(int, input().split())) for _ in range(4)]
    ans = 0
    result = []
    for i in range(4):
        for j in range(4):
            st = str(arr[i][j])
            dfs(i, j, st)
    ans = len(set(result))  # 중복제거
    print(f"#{case} {ans}")
