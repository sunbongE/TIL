def bfs(s, e):
    q = []
    v = [0] * (V + 1)

    q.append(s)
    v[s] = 1

    while q:
        c = q.pop(0)

        if c == e:
            return v[e] - 1

        for n in node[c]:
            # for n in nod:
            if not v[n]:
                q.append(n)
                v[n] = v[c] + 1
    # 목적지에 방문 못한 경우
    return 0


T = int(input())
# V: 노드수, E: 간선수
for case in range(1, 1 + T):
    V, E = map(int, input().split())
    node = [[] for _ in range(V + 1)]

    for _ in range(E):
        a, b = map(int, input().split())
        node[a].append(b)
        node[b].append(a)
    S, G = map(int, input().split())
    # print(S)
    print(f"#{case}", end=" ")
    print(bfs(S, G))
