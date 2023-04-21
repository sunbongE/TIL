from pprint import pprint

# 1 == 흑돌 , 2 == 백돌
T = int(input())
for case in range(1, 1 + T):
    N, M = map(int, input().split())

    arr = [[0] * (N + 1) for _ in range(N + 1)]
    for __ in range(M):
        x, y, dol = map(int, input().split())
        arr[x][y] = dol
        pprint(arr)

# 출력 : 흑돌, 백돌
