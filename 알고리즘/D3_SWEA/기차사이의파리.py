for case in range(1, 1 + int(input())):
    D, A, B, F = map(int, input().split())
    # 총 속도로 전체 거리를 나누면 시간이 나온다.
    # 총 운전 시간이고 여기에 파리 속도를 곱하면 거리가 나온다.
    print(f"#{case}", end=" ")
    print(D / (A + B) * F)
