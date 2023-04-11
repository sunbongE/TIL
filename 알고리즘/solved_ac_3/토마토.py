# 풀이 과정
# 9 8 7 6 5 4
# 8 7 6 5 4 3
# 7 6 5 4 3 2
# 6 5 4 3 2 1
# 최대 값에서 -1 해줘
# 모든 경우에 토마토가 1개 이상은 있다.

# 4방향으로 탐색 후 수정된 배열에 0이 남아있우면 -1 출력한다.
from collections import deque


def bfs():
    while q:
        x, y = q.popleft()

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < n and 0 <= ny < m and box[nx][ny] == 0:
                box[nx][ny] = box[x][y] + 1
                q.append((nx, ny))


m, n = map(int, input().split())
# 토마토가있는 박스
box = [list(map(int, input().split())) for _ in range(n)]

# 익은 토마토의 위치를 찾아 저장한다.
q = deque()
for i in range(n):
    for j in range(m):
        if box[i][j] == 1:
            q.append((i, j))
bfs()

ans = 0
for tomato_list in box:
    for tomato in tomato_list:
        if tomato == 0:
            print(-1)
            exit()
    # print(f"max({ans}, max({tomato_list}))")
    ans = max(ans, max(tomato_list))

print(ans - 1)
# 10

# 1 -1 7  6  5 4
# 0 -1 6  5  4 3
# 9  8 7  6 -1 2
# 0  0 8  7 -1 1

# 1 -1 7 6 5 4
# 2 -1 6 5 4 3
# 3  4 5 6 -1 2
# 4  5 6 7 -1 1
