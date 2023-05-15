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
# print(box)
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
# M, H, N = 5, 2, 3
# v = [[[0] * (M) for _ in range(N)] for _ in range(H)]
# pprint(v)
