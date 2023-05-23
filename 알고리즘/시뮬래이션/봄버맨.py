from collections import deque


def check(t):  # 폭탄 위치 확인.
    for i in range(R):
        for j in range(C):
            if arr[i][j] == "O":
                lst.append((i, j, t + 3))  # 3초 후 터질 시간 기록
    # print(t)
    # print(lst, len(lst))
    return


R, C, N = map(int, input().split())
arr = [list(map(str, input())) for _ in range(R)]
lst = deque()  # 폭탄 위치
check(0)


time = 1  # 1초 시작
while N - time > 0:
    # 1초가 더 흘러 빈칸을 폭탄으로 채우기.
    time += 1
    for i in range(R):
        for j in range(C):
            if arr[i][j] == ".":
                arr[i][j] = "O"
    # 종료 조건 추가
    if N - time == 0:
        break

    flag = True
    while flag:
        time += 1
        while len(lst) > 0:
            # print(lst)
            if lst[0][2] == time:  # 폭발할 시간이면
                # 4방향 폭탄 터짐
                x, y, t = lst.popleft()
                arr[x][y] = "."  # 현위치 폭발
                for di, dj in ((-1, 0), (1, 0), (0, -1), (0, 1)):
                    ni, nj = x + di, y + dj
                    if 0 <= ni < R and 0 <= nj < C:
                        # if arr[ni][nj] == "O":  # 폭탄인경우
                        arr[ni][nj] = "."

            else:  # 폭발할 시간이 아니면 넘어감
                break
        flag = False
    check(time - 1)  # 남은 폭탄 위치 기록.
for a in arr:
    print("".join(a))
