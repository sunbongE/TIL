def dist(way, num):
    result = 0
    if way == 1:  # 북
        result = num
    elif way == 2:  # 남
        result = L + H + L - num
    elif way == 3:  # 서
        result = 2 * (L + H) - num
    else:  # 동
        result = L + num
    return result


L, H = map(int, input().split())
distance = []
N = int(input())
for _ in range(N + 1):
    way, num = map(int, input().split())
    distance.append(dist(way, num))
ans = 0
for i in range(N):
    # 정방향이동, 역방향 이동 수 중 작은 값을 ans +
    dis1 = abs(distance[-1] - distance[i])  # 각 지점 거리의 차이
    dis2 = 2 * (L + H) - dis1  #
    # print(dis1, dis2)
    ans += min(dis1, dis2)
print(ans)
