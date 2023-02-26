from collections import deque

# 큐, 방문, while, base condition


def bfs(f, s, g, u, d):
    q = deque()
    q.append(s)
    v = [0] * (f + 1)
    v[s] = 1
    while q:

        cur = q.popleft()
        if cur == g:
            return v[g] - 1

        for val in (cur + u, cur - d):
            if 1 <= val <= f and not v[val]:
                q.append(val)
                v[val] = v[cur] + 1

    return "use the stairs"


# 층수, 현위치, 목적지, 업, 다운
F, S, G, U, D = list(map(int, input().split()))

print(bfs(F, S, G, U, D))
