# 내리막길.
from pprint import pprint

# 4방향 탐색
# 항상 작은 값으로 이동.
M, N = map(int, input().split())

arr = [[10000] * (N + 1)] + [
    [10000] + list(map(int, input().split())) for _ in range(M)
]
dp = [[0] * (N + 1) for _ in range(M + 1)]
way = [[0] * (N + 1) for _ in range(M + 1)]
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
way[1][1] = 1
dp[1][1] = 1
# print("dp", dp)
# print("way", way)
# print("arr", arr)
for i in range(1, M + 1):
    for j in range(1, N + 1):
        # 전에 값이 현재 위치의 값의 전에 값의 위치를 way에 저장한 인덱스를 사용해서 비교
        if (
            dp[i][j] > 0 and arr[i][j] < arr[i - di[way[i][j]]][j - dj[way[i][j]]]
        ):  # 갈수 있는 경로이고 전에 값보다 작다면
            prev = arr[i][j]  # arr[i - di[way[i][j]]][j - dj[way[i][j]]]
            # 4방향 탐색
            for d_idx in range(4):
                ni, nj = i + di[d_idx], j + dj[d_idx]

                if 0 <= ni < M and 0 <= nj < N and arr[ni][nj] < prev:
                    # 탐색 방향이 범위내, 내리막
                    way[ni][nj] = d_idx
                    dp[ni][nj] += dp[i][j]  # 전에 값을 더해준다.
                    # print(ni, nj)
pprint(dp)
pprint(way)
