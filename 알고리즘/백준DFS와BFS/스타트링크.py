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

        for val in (cur + u, cur - d):  # 올라간거 내려간거 체크.
            if 1 <= val <= f and not v[val]:  # 이동한 곳이 범위 내면
                q.append(val)  # 큐 삽입
                v[val] = v[cur] + 1  # 방문횟수 += 1
                print(v, val)

    return "use the stairs"


# 층수, 현위치, 목적지, 업, 다운
F, S, G, U, D = list(map(int, input().split()))

print(bfs(F, S, G, U, D))
