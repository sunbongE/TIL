def check(R, C):
    for i in range(1, len(R)):
        if R[i] - R[i - 1] != 1:
            return False
    for i in range(1, len(C)):
        if C[i] - C[i - 1] != 1:
            return False
    return True


for case in range(1, 1 + int(input())):
    status = "yes"
    N = int(input())
    arr = [list(map(str, input())) for _ in range(N)]
    new_arr = list(map(list, zip(*arr)))
    R = []  # 행
    C = []  # 열
    for i in range(N):
        # 가로
        if "#" in arr[i]:
            R.append(i)
        # 세로
        if "#" in new_arr[i]:
            C.append(i)
    if not check(R, C):  # 붙어있는 사각형인지 확인
        status = "no"

    else:  # 이제 개수확인
        R_val = R[-1] - R[0] + 1  # 가로길이
        C_val = C[-1] - C[0] + 1  # 세로 길이
        area = R_val * C_val  # 사각형 넓이
        cnt = 0
        if R_val != C_val:  # 정사각형인지 확인.
            status = "no"
        else:
            for i in range(R[0], R[-1] + 1):
                for j in range(C[0], C[-1] + 1):
                    if arr[i][j] == "#":
                        cnt += 1
            if cnt != area:
                status = "no"

    print(f"#{case} {status}")
