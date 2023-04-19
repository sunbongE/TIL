# 1860 진기의 최고급 붕어빵

# M초에 K개의 붕어빵 만듬
# N = 정수의 개수

for case in range(1, int(input()) + 1):
    ans = "Possible"
    N, M, K = map(int, input().split())
    arrival = list(map(int, input().split()))
    arrival.sort()
    cnt = 0
    for t in arrival:
        cnt += 1  # 들어온 사람의 수
        if t // M * K < cnt:  # 들어온 사람의 수가 더 많으면 기다려야하는 상황
            ans = "Impossible"
            break
    print(ans)
