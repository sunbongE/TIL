# 격자판 특징을 이용한 문제..
# 격자판에서 (0,0)을 포함하여 대각선으로 서로 인접한 칸들은 서로 색이 다르다.
# 격자판을 2차원으로 하여 각 칸의 (col+row)합이 홀수인 칸들과 짝수인 칸들의 색이
# 서로 다르다는 것을 의미한다.
#
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    board = [0, 0, 0, 0]

    for col in range(N):
        for row in range(M):
            if arr[col][row] == "#":
                if (col + row) % 2 == 0:
                    board[0] += 1
                elif (col + row) % 2 == 1:
                    board[1] += 1
            elif arr[col][row] == ".":
                if (col + row) % 2 == 0:
                    board[2] += 1
                elif (col + row) % 2 == 1:
                    board[3] += 1
    # 격자판에서 대각선의 값이 서로 같아야하기 때문에 [0] and [2] , [1] and [3] 이 조건이 만족하면 안된다.
    #
    if (
        (board[0] and board[1])
        or (board[2] and board[3])
        or (board[0] and board[2])
        or (board[1] and board[3])
    ):
        answer = "impossible"
    else:
        answer = "possible"
    print(board)
    print(f"#{t+1}", answer)
