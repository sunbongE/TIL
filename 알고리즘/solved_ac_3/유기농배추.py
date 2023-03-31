# DFS 전체가 방문될 때 까지 반복하고 매 반복 후 cnt +=1 하면 원하는 값을 알수 있다.
# v = [[2, 4], [2], [0, 1, 2, 2, 3, 4], [2], [2, 0]]

dirR = [1, -1, 0, 0]
dirC = [0, 0, 1, -1]
MAX = 50 + 10


def dfs(y, x):
    visited[y][x] = 1
    for diridx in range(4):
        newY = y + dirR[diridx]
        newX = x + dirC[diridx]
        if graph[newY][newX] and not visited[newY][newX]:
            dfs(newY, newX)


tc = int(input())
for _ in range(tc):
    cnt = 0
    m, n, k = map(int, input().split())
    graph = [[0] * MAX for _ in range(MAX)]
    visited = [[0] * MAX for _ in range(MAX)]
    for _ in range(k):
        x, y = map(int, input().split())  # 좌표입력
        graph[y + 1][x + 1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if graph[i][j] and not visited[i][j]:
                dfs(i, j)
                cnt += 1
    print(cnt)
