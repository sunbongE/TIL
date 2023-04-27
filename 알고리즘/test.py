N, M = map(int, input().split())
graph = [list(input().rstrip()) for _ in range(N)]
dx, dy = [0, 0, -1, 1], [-1, 1, 0, 0]


def check(i, j):
    for k in range(4):
        x = j + dx[k]
        y = i + dy[k]
        if 0 <= y < N and 0 <= x < M:
            if graph[y][x] == "W":
                return False
            elif graph[y][x] == ".":
                graph[y][x] = "D"
    return True


def search():
    for i in range(N):
        for j in range(M):
            if graph[i][j] == "S":
                if not check(i, j):
                    return False
    return True


if search():
    print(1)
    for grap in graph:
        print("".join(grap))
else:
    print(0)
