for case in range(1, int(input()) + 1):
    N, Q = map(int, input().split())
    li = [0] * N
    for i in range(Q):
        L, R = map(int, input().split())
        for j in range(L - 1, R):
            li[j] = i + 1
    print(f"#{case}", end=" ")
    print(*li)
