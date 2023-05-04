# from pprint import pprint


def bfs(si, sj):
    v = [[0] * 16 for _ in range(16)]
    q = []

    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.pop(0)
        if arr[ci][cj] == 3:
            return True
        for di, dj in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            ni, nj = ci + di, cj + dj
            if arr[ni][nj] != 1 and v[ni][nj] == 0:  # 미방문 갈수있는길.
                q.append((ni, nj))
                v[ni][nj] = 1
    # pprint(v)
    return False


for _ in range(10):
    case = int(input())
    arr = [list(map(int, input())) for _ in range(16)]
    # print(arr)
    for i in range(1, 15):
        for j in range(1, 15):
            if arr[i][j] == 2:
                ans = bfs(i, j)
                break

    if ans:
        print(f"#{case} 1")
    else:
        print(f"#{case} 0")
