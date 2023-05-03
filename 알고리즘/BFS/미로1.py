import sys

sys.stdin = open("미로1.txt")


def bfs(si, sj):
    q = []
    v = [[0] * N for _ in range(N)]

    # q에 초기 데이터 삽입, v표시
    q.append((si, sj))
    # 도착여부,,
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        if arr[ci][cj] == 3:
            return v[ci][cj]

        # 네방향 방문    상 하 좌 우
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            # 범위안에 있고, 방문을 안했고, 벽이 아니면
            if 0 <= ni < N and 0 <= nj < N and v[ni][nj] == 0 and arr[ni][nj] != 1:
                q.append((ni, nj))
                v[ni][nj] = 1
    return 0


T = 10
for test_case in range(1, T + 1):
    case = input()
    N = 16
    arr = [list(map(int, input())) for _ in range(N)]  # 배열입력
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 2:  # 시작위치 찾음
                si, sj = i, j
    ans = bfs(si, sj)
    print(f"#{test_case} {ans}")

# ---------------------------------------------------------
# 미로찾기
from pprint import pprint
from collections import deque


def bfs(x, y):
    q = deque()
    q.append((x, y))
    v[x][y] = 1

    while q:
        cx, cy = q.popleft()
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < n and 0 <= ny < n and arr[nx][ny] != 1 and v[nx][ny] == 0:
                q.append((nx, ny))
                v[nx][ny] = v[cx][cy] + 1


for case in range(1, 1 + int(input())):
    ans = 0
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    v = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 2:
                bfs(i, j)
            if arr[i][j] == 3:
                ex, ey = i, j
    if v[ex][ey] != 0:
        ans = v[ex][ey] - 2
    print(f"#{case} {ans}")
