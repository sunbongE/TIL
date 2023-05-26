from pprint import pprint
from collections import deque


def bfs(si, sj):
    global cnt
    q = deque()
    q.append((si, sj))
    arr[si][sj] = 1
    cnt += 1

    while q:
        ci, cj = q.popleft()
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < M and 0 <= nj < N and not arr[ni][nj]:
                arr[ni][nj] = 1
                cnt += 1
                q.append((ni, nj))
    return


M, N, K = map(int, input().split())
arr = [[0] * (N) for _ in range(M)]
# pprint(arr)
for _ in range(K):
    y1, x1, y2, x2 = map(int, input().split())
    for i in range(x1, x2):
        for j in range(y1, y2):
            arr[i][j] = 1
ans = []
L = 0
for ii in range(M):
    for jj in range(N):
        if arr[ii][jj] == 0:
            cnt = 0
            L += 1
            bfs(ii, jj)
            ans.append(cnt)
ans.sort()
print(L)
print(*ans)
