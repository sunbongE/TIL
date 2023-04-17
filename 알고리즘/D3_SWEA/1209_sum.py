for case in range(1, 11):
    c = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    ans = 0
    n_arr = dict()
    # 세로 생성
    for i in range(100):
        for j in range(100):
            if j not in n_arr:
                n_arr[j] = [arr[i][j]]
            else:
                n_arr[j] += [arr[i][j]]

    # 가로 연산
    for i in range(100):
        temp = sum(arr[i])
        ans = max(ans, temp)
        temp = sum(n_arr[i])
        ans = max(ans, temp)

    # 대각선 왼-위 => 오른-아래
    temp = 0
    for i in range(100):
        temp += arr[i][i]
    ans = max(ans, temp)

    # 대각선 오른-위 => 왼-아래
    temp = 0
    for i in range(100):
        temp += arr[i][100 - i - 1]
    ans = max(ans, temp)
    print(f"#{case} {ans}")
# ----------
# 아래 풀이가 더 좋음
for _ in range(1):
    i = int(input())
    m = [list(map(int, input().split())) for _ in range(5)]

    box = []
    # 가로 / 세로
    for a1 in range(5):
        a = 0
        b = 0
        for a2 in range(5):
            a += m[a1][a2]
            b += m[a2][a1]
        box.append(a)
        box.append(b)

    # 대각선
    c = 0
    d = 0
    for a1 in range(5):
        c += m[a1][a1]
        d += m[a1][4 - a1]
    box.append(c)
    box.append(d)
    print(box)
    print("#{} {}".format(i, max(box)))
