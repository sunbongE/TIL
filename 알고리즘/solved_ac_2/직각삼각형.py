while 1:
    abc = list(map(int, input().split()))
    if abc == [0, 0, 0]:  # 멈추는 조건
        break

    abc.sort()  # 정렬한다.

    if (abc[0] ** 2 + abc[1] ** 2) == abc[2] ** 2:
        print("right")
    else:
        print("wrong")
