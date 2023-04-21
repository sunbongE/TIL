from pprint import pprint

# # 1 == 흑돌 , 2 == 백돌

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [[0] * (N + 1) for _ in range(N + 1)]
    m = N // 2
    arr[m][m] = arr[m + 1][m + 1] = 2
    arr[m][m + 1] = arr[m + 1][m] = 1

    for _ in range(M):
        si, sj, d = map(int, input().split())
        arr[si][sj] = d
        for di, dj in (
            (-1, -1),
            (-1, 0),
            (-1, 1),
            (1, -1),
            (1, 0),
            (1, 1),
            (0, -1),
            (0, 1),
        ):
            re = []
            for mul in range(1, N):
                ni, nj = si + di * mul, sj + dj * mul
                if 1 <= ni <= N and 1 <= nj <= N:  # 범위안에
                    if arr[ni][nj] == 0:  # 0이면 빠꾸
                        break
                    elif arr[ni][nj] == d:  # 같은 돌 발견
                        while re:  # 변경 후보에 있는 거 변경
                            ti, tj = re.pop()
                            arr[ti][tj] = d
                        break
                    else:  # 다른 돌이면 변경후보에 추가
                        re.append((ni, nj))
                else:  # 범위 밖이면 멈춰
                    break
    B = W = 0
    for lst in arr:
        B += lst.count(1)
        W += lst.count(2)
    print(arr)
    print("#{} {} {}".format(test_case, B, W))

    # 돌을 두고 4방향 탐색으로 현재 돌과 다르면서 0이 아니면
    # 그 방향으로 전진
    # 전진 cnt기록, 전진 하다가 2를 만나면 cnt만큼 반복문을 통해
    # 지나온 값을 바꿔준다.
    #

# 출력 : 흑돌, 백돌
