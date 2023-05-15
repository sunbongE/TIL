def dfs(d, idx):
    global ans
    if d == N // 2:
        # print(v, d + 1, 1 + idx)
        start, link = 0, 0
        for i in range(N):
            for j in range(N):
                if v[i] and v[j]:
                    start += S[i][j]
                elif not v[i] and not v[j]:
                    link += S[i][j]
        # print(start,link)
        ans = min(ans, abs(start - link))
        return

    for i in range(idx, N):
        if not v[i]:
            v[i] = 1
            dfs(d + 1, i + 1)
            v[i] = 0


N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
v = [0] * N
ans = float("inf")
dfs(0, 0)
print(ans)
