# from pprint import pprint
import sys

sys.setrecursionlimit(10**6)  # 재귀함수 깊이설정! 이거안하면 안풀림
input = sys.stdin.readline


def dfs(x, y):
    visited[x][y] = 1  # 방문표시
    for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:  # 4방향탐색
        nx = x + dx
        ny = y + dy
        if arr[nx][ny] == 1 and not visited[nx][ny]:
            dfs(nx, ny)


T = int(input())
for _ in range(T):  # 테스트 케이스만큼 반복
    m, n, k = map(int, input().split())  # 가로, 세로, 좌표개수
    arr = [[0] * (m + 1) for _ in range(n + 1)]
    visited = [[0] * (m + 1) for _ in range(n + 1)]
    for _ in range(k):  # 좌표 입력받아 1표시
        x, y = map(int, input().split())
        arr[y][x] = 1
    cnt = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j] and not visited[i][j]:  # 배열에 값이 1이고, 미방문
                dfs(i, j)
                cnt += 1
    print(cnt)
