def solve(ci, cj, dr):
    cnt = 0
    while 1:
        arr[ci][cj] = 2
        cnt += 1

        flag = 1
        while flag == 1:
            for nd in [(dr + 3) % 4, (dr + 2) % 4, (dr + 1) % 4, dr]:  # 반시계 방향으로 탐색
                ni, nj = ci + di[nd], cj + dj[nd]
                if arr[ni][nj] == 0:  # 빈칸이면
                    ci, cj, dr = ni, nj, nd  # 위치와 방향을 갱신한다.
                    flag = 0
                    break
            else:  # 모든 방향이 청소됐으면 후진
                bi, bj = ci - di[dr], cj - dj[dr]
                if arr[bi][bj] == 1:  # 후진 못하면 리턴
                    return cnt
                else:
                    ci, cj = bi, bj  # 후진.


N, M = map(int, input().split())
r, c, d_idx = map(int, input().split())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
arr = [list(map(int, input().split())) for _ in range(N)]

ans = solve(r, c, d_idx)  # 항상 빈칸이니까 청소함.

print(ans)
