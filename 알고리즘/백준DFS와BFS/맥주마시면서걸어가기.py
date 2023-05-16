from collections import deque


def bfs(si, sj, ei, ej):
    q = deque()
    q.append((si, sj))
    v = [0] * N  # 편의점 방문 표시..

    while q:
        ci, cj = q.popleft()
        if abs(ci - ei) + abs(cj - ej) <= 1000:  # 목적지까지 거리가 된다면 끝낸다.
            return "happy"
        for i in range(N):  # 현재 위치에서 다음 편이점 위치를 계산한 것.
            ti, tj = li[i]
            if abs(ci - ti) + abs(cj - tj) <= 1000 and not v[i]:
                v[i] = 1
                q.append((ti, tj))
    return "sad"


for case in range(int(input())):
    N = int(input())
    si, sj = map(int, input().split())  # 집위치
    li = []  # 편의점 위치 정장.
    for _ in range(N):
        a, b = map(int, input().split())
        li.append((a, b))
    ei, ej = map(int, input().split())  # 끝 위치
    print(bfs(si, sj, ei, ej))
