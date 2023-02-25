from collections import deque


def bfs(si, sj, h):
    q = deque()

    q.append((si, sj))
    v[si][sj] = 1

    while q:
        ci, cj = q.popleft()
        # 네방향, 범위내, 미방문, 높이>h
        for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
            ni, nj = ci + di, cj + dj
            if 0 <= ni < N and 0 <= nj < N and not v[ni][nj] and arr[ni][nj] > h:
                q.append((ni, nj))
                v[ni][nj] = 1


def solve(h):  # 0~99 까지 높이
    cnt = 0  # 안전영역 개수
    for i in range(N):
        for j in range(N):
            if not v[i][j] and arr[i][j] > h:
                bfs(i, j, h)
                cnt += 1
        if cnt == 0:  # 0이 되면 가장 큰 높이까지 물에 잠기는 것이라서 멈춘다.
            break
        # print(cnt, h)
    return cnt


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for h in range(100):  # 0~99 까지 높이
    v = [[0] * N for i in range(N)]  # 각 높이마다 방문 초기화
    ans = max(ans, solve(h))
print(ans)
