from collections import deque
from pprint import pprint


def dfs(i, j, sm):
    global ans
    ans = max(sm, ans)
    v[ord(arr[i][j]) - 65] = 1
    for idx in range(4):
        ni, nj = i + d[idx][0], j + d[idx][1]
        if 0 <= ni < N and 0 <= nj < K and not v[ord(arr[ni][nj]) - 65]:
            v[ord(arr[ni][nj]) - 65] = 1
            dfs(ni, nj, sm + 1)
            v[ord(arr[ni][nj]) - 65] = 0


ans = 0
idx = 0
d = [(0, 1), (-1, 0), (1, 0), (0, -1)]
N, K = map(int, input().split())
arr = [list(map(str, input())) for _ in range(N)]
v = [0] * 27
for start in range(1, 2):
    dfs(0, 0, 1)
print(ans)

# print(ord("A")) # 65
