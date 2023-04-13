# # RGB거리,,,,
# #


# # 최소 비용
# # 빨 초 파
# # 26 40 83
# # 49 60 57
# # 13 89 99

# # 26 57 = 83+13 = 96

# # 각 위치의 드는 비용을 구하고 물론 내가 있던 위치빼고
# # min으로 최소값을 찾아
# # 반복문이 끝나면 최신화가 된 리스트에서 또 min하면 답
# n = int(input())
# homes = [list(map(int, input().split())) for _ in range(n)]
# # print(homes)
# for i in range(1, n):
#     # print(homes[i])
#     homes[i][0] = homes[i][0] + min(homes[i - 1][1], homes[i - 1][2])
#     homes[i][1] = homes[i][1] + min(homes[i - 1][2], homes[i - 1][0])
#     homes[i][2] = homes[i][2] + min(homes[i - 1][1], homes[i - 1][0])
# print(min(homes[-1]))
# # print(homes)
dx = [0, 1, 1, 1]  # 우 하 우하 좌하
dy = [1, 0, 1, -1]


def Omok(matrix):
    for i in range(N):
        for j in range(N):
            if matrix[i][j] == "o":
                for idx in range(4):
                    cnt = 1
                    nx = i + dx[idx]
                    ny = j + dy[idx]

                    while 1:
                        if -1 < nx < N and -1 < ny < N and matrix[nx][ny] == "o":
                            nx, ny = nx + dx[idx], ny + dy[idx]
                            cnt += 1
                        else:
                            break

                    if cnt >= 5:
                        return "YES"

    return "NO"


for tc in range(1, T + 1):
    answer = 0
    N = int(input())
    matrix = [list(input()) for _ in range(N)]

    print(f"#{tc} {Omok(matrix)}")
