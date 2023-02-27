from collections import deque
import sys

input = sys.stdin.readline


def bfs(si, sj, v):
    q = deque()
    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()

        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = di + ci, dj + cj
            if arr[ni][nj] > 0 and v[ni][nj] == 0:
                q.append((ni, nj))
                v[ni][nj] = 1


def solve():
    for year in range(1, 900000):  # 최악의 경우로 값을 구해야해서 행,열 최대300  10
        # 네방향 개수 카운트
        a_sub = [[0] * M for _ in range(N)]
        for i in range(1, N - 1):
            for j in range(1, M - 1):
                if arr[i][j] == 0:
                    continue
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = i + di, j + dj
                    if arr[ni][nj] == 0:  # 4방향 탐색해서 0이면 1증가하여 뺄 값을 기록한다.
                        a_sub[i][j] += 1
        # 높이 맞추기
        for i in range(1, N - 1):
            for j in range(1, M - 1):
                if a_sub[i][j] > 0:
                    arr[i][j] = max(0, arr[i][j] - a_sub[i][j])  # 음수 방지

        # 빙산 덩어리 개수 카운트
        v = [[0] * M for _ in range(N)]
        cnt = 0
        for i in range(1, N - 1):
            for j in range(1, M - 1):
                if arr[i][j] > 0 and not v[i][j]:
                    bfs(i, j, v)
                    cnt += 1
                    if cnt > 1:
                        return year
        if cnt == 0:
            return 0


N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

ans = solve()
print(ans)
