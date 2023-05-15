from collections import deque


def bfs():
    cnt = 0
    q = deque()
    v = [[[0] * M for _ in range(N)] for _ in range(H)]

    for h in range(H):
        for i in range(N):
            for j in range(M):
                if arr[h][i][j] == 1:
                    v[h][i][j] = 1
                    q.append((h, i, j))

                elif arr[h][i][j] == 0:
                    cnt += 1

    while q:
        ch, ci, cj = q.popleft()
        # 6방향, 범위내, 미방문, 안익은 토마토
        #                   상       하       좌      우       위     아래
        for dh, di, dj in (
            (0, -1, 0),
            (0, 1, 0),
            (0, 0, -1),
            (0, 0, 1),
            (-1, 0, 0),
            (1, 0, 0),
        ):
            nh, ni, nj = ch + dh, ci + di, cj + dj
            if (
                0 <= nh < H
                and 0 <= ni < N
                and 0 <= nj < M
                and arr[nh][ni][nj] == 0
                and v[nh][ni][nj] == 0
            ):
                q.append((nh, ni, nj))
                v[nh][ni][nj] = v[ch][ci][cj] + 1
                cnt -= 1
    if cnt == 0:
        return v[ch][ci][cj] - 1
    else:
        return -1


M, N, H = map(int, input().split())
arr = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
ans = bfs()
print(ans)

# ==========================내풀이===========================================================
from pprint import pprint
from collections import deque


def bfs():
    global check
    while q:
        ch, ci, cj = q.popleft()
        for dh, di, dj in [
            (-1, 0, 0),
            (1, 0, 0),
            (0, -1, 0),
            (0, 1, 0),
            (0, 0, -1),
            (0, 0, 1),
        ]:
            nh, ni, nj = ch + dh, ci + di, cj + dj
            if 0 <= nh < H and 0 <= ni < N and 0 <= nj < M:  # 범위내
                if box[nh][ni][nj] == 0:  # 안익었고 방문안했으면
                    box[nh][ni][nj] = box[ch][ci][cj] + 1  # 몇일이 지나서 익는지 기록
                    check -= 1  # 안익은 토마토 개수 -= 1
                    q.append((nh, ni, nj))  # 순회 대상 큐에 추가.
    return


# 가로 세로 높이.
M, N, H = map(int, input().split())
q = deque()
box = [[[] for _ in range(N)] for _ in range(H)]

check = 0  # 안 익은 토마토 수 확인
for ii in range(H):
    for jj in range(N):
        line = list(map(int, input().split()))
        for j in range(M):  # 익은 토마토의 위치를 기록해둔다.
            if line[j] == 1:
                q.append((ii, jj, j))
        box[ii][jj] += line
        if 0 in line:
            check += line.count(0)
if check:  # 안익은게 있으면
    day = 0
    bfs()
    if check:  # 안익은 토마토가 남았으면
        print(-1)
    else:  # 익은 토마토가 몇일만에 익었는지 확인.
        for line in box:
            for tomatos in line:
                day = max(day, max(tomatos))
        print(day - 1)
else:
    print(0)
