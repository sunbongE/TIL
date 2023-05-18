import math

T = int(input())
ans = []

for t in range(T):
    N = int(input())
    tot = 0  # 라운드 마다의 총점
    for n in range(N):
        x, y = map(int, input().split())
        p = math.ceil(math.sqrt(x * x + y * y) / 20)
        if p <= 0:
            tot += 10
        elif p <= 11:
            tot += 11 - p
    ans.append(f"#{t + 1} {tot}")

for x in ans:
    print(x)
