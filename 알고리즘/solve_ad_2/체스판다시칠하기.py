N, M = map(int, input().split())
ans = []
board = []
for _ in range(N):
    board.append(input())


for i in range(N - 7):
    for j in range(M - 7):
        A = 0
        B = 0

        for a in range(i, i + 8):
            for b in range(j, j + 8):
                if (a + b) % 2 == 0:
                    if board[a][b] != "B":
                        A += 1
                    if board[a][b] != "W":
                        B += 1
                else:
                    if board[a][b] != "W":
                        A += 1
                    if board[a][b] != "B":
                        B += 1
        ans.append(A)
        ans.append(B)

print(min(ans))
