def dfs(node, visited):
    visited[node] = True
    max_length = 0
    for next_node in graph[node]:
        if not visited[next_node]:
            length = dfs(next_node, visited)
            max_length = max(max_length, length)
    visited[node] = False
    return max_length + 1


t = int(input())
for test_case in range(1, t + 1):
    n, m = map(int, input().split())
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    max_length = 0
    for start_node in range(1, n + 1):
        visited = [False] * (n + 1)
        length = dfs(start_node, visited)
        max_length = max(max_length, length)
    print(f"#{test_case} {max_length}")
