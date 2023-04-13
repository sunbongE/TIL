t = int(input())

for _ in range(t):
    N, K = map(int, input().split())

    arr = [list(map(int, input().split())) for __ in range(N)]
    ans = 0
    # 가로 탐색
    for i in range(N):
        temp = 0
        for j in range(N):
            if arr[i][j] == 1:
                temp += 1
            else:
                if temp == K:
                    ans += 1
                temp = 0
        if temp == K:
            ans += 1
    # 세로 탐색
    for ii in range(N):
        temp = 0
        for jj in range(N):
            if arr[jj][ii] == 1:
                temp += 1
            else:
                if temp == K:
                    ans += 1
                temp = 0
        if temp == K:
            ans += 1
            temp = 0

    print(f"#{_+1} {ans}")
