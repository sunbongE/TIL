from pprint import pprint


def check(x, y):
    global ans
    cnt = 0
    for di in range(4):
        nx, ny = x + dx[di], y + dy[di]
        if arr[nx][ny] == 1:
            cnt += 1
    if cnt == 2:  # 모서리
        ans += 2
    elif cnt == 3:
        ans += 1
    return


ans = 0
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
n = int(input())
arr = [[0] * 101 for _ in range(101)]
for _ in range(n):
    x, y = map(int, input().split())

    for i in range(y, y + 10):
        for j in range(x, x + 10):
            arr[i][j] = 1
# 1로 표시된 4방향 탐색
for i in range(101):
    for j in range(101):
        if arr[i][j] == 1:
            check(i, j)
print(ans)
