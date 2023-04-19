d = [0]  # 속도 줄이려는 목적 - 예전 테케에서 계산한 적 있는 대각선이면 값만 찾아올것


def find(n):
    global d
    print(d)
    if n <= d[-1]:  # 예전에 찾았던 적 있는 대각선이면
        k = len(d)  # k를 마지막 대각선에서 출발해서 감소시킴
        for i in range(len(d) - 1, -1, -1):
            if d[i - 1] < n <= d[i]:
                k = i  # k의 의미 : i번째 대각선에 그 점이 포함되어있다
                break
        return [
            1 + n - (1 + (k - 1) * k // 2),
            k - (n - (1 + (k - 1) * k // 2)),
        ]  # 시작,끝점 규칙에 따라 계산
    else:
        k = len(d)  # 예전에 찾지않았던 큰 숫자면 새로 계산해야함
        while True:
            if (1 + (k - 1) * k // 2) <= n <= k * (k + 1) // 2:
                break
            d.append(k * (k + 1) // 2)  # 이 대각선의 끝점을 d에 기록해놓기
            k += 1
        return [1 + n - (1 + (k - 1) * k // 2), k - (n - (1 + (k - 1) * k // 2))]


res = []
for tc in range(int(input())):
    P, Q = map(int, input().split())
    p_xy = find(P)
    q_xy = find(Q)
    xy = [p_xy[0] + q_xy[0], p_xy[1] + q_xy[1]]
    r = 1 + (xy[0] + xy[1] - 1) * (xy[0] + xy[1] - 2) // 2 + xy[0] - 1
    res.append("#{} {}".format(tc + 1, r))
print("\n".join(res))
