def dfs(c, v):
    global ans
    # print(v)
    ans = max(ans, len(v))
    for n in li[c]:
        if n not in v:
            dfs(n, v + [n])


for case in range(1, int(input()) + 1):
    ans = 0
    N, M = map(int, input().split())

    li = [[] for _ in range(N + 1)]

    for _ in range(M):
        s, e = map(int, input().split())
        li[s].append(e)
        li[e].append(s)
    # print(li)
    for s in range(1, N + 1):
        dfs(s, [s])
    print(f"#{case} {ans}")
