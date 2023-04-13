#    위 오른쪽위    우   우아래 아래  왼아래   좌    왼위
# [(-1,0),(-1,1), (0,1),(1,1), (1,0),(1,-1),(0,-1),(-1,-1)]
# 대각선
# 오른쪽 위에
# 오른쪽 아래 (1,1)
# 외쪽 위에 (-1,-1)
# 외쪽 아래
# 8방향 탐색인데 언제하냐면
# 일단 입력 받은 배열에서 'o' 을 찾으면 dfs보내서 8방향을 쭉 살핀다.
# if arr[nx][ny] == 'o' 이라면 cnt += 1 dfs ㄱㄱ
# else : 방향 바꿔서 다시 dfsㄱㄱ

dn = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]


def dfs(x, y, N, idx):
    global cnt, ans
    if cnt >= 5:
        ans = "YES"
        return ans

    nx = x + dn[idx][0]
    ny = y + dn[idx][1]
    if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] == "o":
        # print(nx, ny)
        cnt += 1
        dfs(nx, ny, N, idx)
    else:
        idx = idx + 1
        if idx == 8:
            return False
        cnt = 1
        dfs(x, y, N, idx)


T = int(input())
for _ in range(T):  # 테케만큼 반복하고
    ans = "NO"
    N = int(input())  # 오목 사이즈 받고
    arr = [list(map(str, input())) for __ in range(N)]  # 오목상황 받고

    # 탐색하면서 'o' 찾기.
    for i in range(N):
        for j in range(N):
            if arr[i][j] == "o":
                cnt = 1
                status = dfs(i, j, N, 0)
    if cnt == status:
        print(f"#{_+1} {ans}")
    else:
        print(f"#{_+1} {ans}")
