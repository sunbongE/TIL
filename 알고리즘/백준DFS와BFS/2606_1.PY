def dfs(c):
    global ans
    ans += 1

    v[c] = 1
    for n in arr[c]:
        if not v[n]:
            dfs(n)


N = int(input())

arr = [[] for _ in range(N + 1)]

v = [0] * (N + 1)


for _ in range(int(input())):
    s, e = map(int, input().split())
    arr[s].append(e)
    arr[e].append(s)

ans = 0

dfs(1)
print(ans - 1)
