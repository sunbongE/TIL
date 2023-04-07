from collections import deque
import sys

input = sys.stdin.readline
m, n = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(n)]
q = deque()


def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
                arr[nx][ny] = arr[x][y] + 1
                q.append((nx, ny))


for i in range(n):
    for j in range(m):
        if arr[i][j] == 1:
            q.append((i, j))
bfs()
ans = 0
for tomatos in arr:
    for tomato in tomatos:
        if tomato == 0:
            print(-1)
            exit()
    ans = max(ans, max(tomatos))
print(ans - 1)
