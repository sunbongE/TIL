def dfs(row, col, jump):
    cur_paper = paper[row][col]

    for r in range(row, row + jump):
        for c in range(col, col + jump):
            if cur_paper != paper[r][c]:  # 다음 종이랑 시작 종이가 다르면.
                # 9등분 해줘야한다.
                j = jump // 3
                # 각각 범위를 정해서 호출한다.
                dfs(row, col, j)  # 1~3번째 줄 1~3 까지
                dfs(row, col + j, j)  # 1~3번째 줄 4~6 까지
                dfs(row, col + j * 2, j)  # 1~3번째 줄 7~9 까지

                dfs(row + j, col, j)  # 4~6번째 줄 1~3 까지
                dfs(row + j, col + j, j)  # 4~6번째 줄 4~6 까지
                dfs(row + j, col + j * 2, j)  # 4~6번째 줄 7~9 까지

                dfs(row + j * 2, col, j)  # 7~9번째 줄 1~3 까지
                dfs(row + j * 2, col + j, j)  # 7~9번째 줄 4~6 까지
                dfs(row + j * 2, col + j * 2, j)  # 7~9번째 줄 7~9 까지
                return
    # 위 과정을 통과후 한 가지 종이로만 된 경우
    ans[cur_paper] += 1
    return


ans = {-1: 0, 0: 0, 1: 0}
n = int(input())

paper = [list(map(int, input().split())) for _ in range(n)]
dfs(0, 0, n)
for a in ans.values():
    print(a)
