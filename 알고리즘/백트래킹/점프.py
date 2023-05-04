from pprint import pprint

# 점프
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
dp = [[0] * N for _ in range(N)]  # 경우 기록
dp[0][0] = 1

# 시작 위치에서 아래나 오른쪽으로 이동한 위치에 표시를 한다.
# 이동은 밟고있는 위치에 번호만큼 한다.
# (0,0) => (n-1,n-1) 까지 이동하는건데
# 경로에 몇 가지 경우인지 기록을 하면서 넘어가면
# 마지막 위치에 전체 경우가 기록되는거

for i in range(N):
    for j in range(N):
        # 현재 위치가 점프할 수 있고, 경우의 수가 있다면
        if arr[i][j] > 0 and dp[i][j] > 0:
            jump = arr[i][j]
            #               아래   오른쪽
            for di, dj in [(jump, 0), (0, jump)]:
                ni, nj = i + di, j + dj
                if ni < N and nj < N:  # 이동 위치가 범위내
                    dp[ni][nj] += dp[i][j]
# pprint(dp)
print(dp[N - 1][N - 1])
