for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    # 두 직사각형이 겹치지 않는 경우
    if x1 > p2 or x2 > p1 or y1 > q2 or y2 > q1:
        print("d")
    # 두 직사각형이 겹치는 경우
    else:
        # 겹치는 부분이 점인 경우
        if (
            (x1 == p2 and y1 == q2)
            or (x1 == p2 and y2 == q1)
            or (x2 == p1 and y1 == q2)
            or (x2 == p1 and y2 == q1)
        ):
            print("c")
        # 겹치는 부분이 선분인 경우
        elif x1 == p2 or x2 == p1 or y1 == q2 or y2 == q1:
            print("b")
        # 겹치는 부분이 직사각형인 경우
        else:
            print("a")
