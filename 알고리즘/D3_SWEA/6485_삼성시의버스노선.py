for case in range(1, 1 + int(input())):
    N = int(input())
    way = []  # 노선 정보
    for _ in range(N):
        way.append(list(map(int, input().split())))
    P = int(input())
    stations = []  # 정류장정보
    for __ in range(P):
        stations.append(int(input()))

    result = [0] * P
    # 풀이..
    # 정류장을 순회
    for i in range(P):
        # 노선 순회?
        for a, b in way:
            # 정류장이 노선범위 안에 있는지 확인해서 있으면 +1 한다.
            if a <= stations[i] <= b:
                result[i] += 1
    print(f"#{case}", end=" ")
    print(*result)
