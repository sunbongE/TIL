T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for __ in range(N)]
    ans = 0
    for ii in range(N - M + 1):
        for jj in range(N - M + 1):
            temp = 0
            for i in range(ii, ii + M):
                for j in range(jj, jj + M):
                    temp += arr[i][j]
            ans = max(ans, temp)
    print(f"#{_+1} {ans}")
