t = int(input())
for case in range(1, 1 + t):
    N = int(input())
    ans = 0
    for _ in range(N):
        p, x = map(float, input().split())
        ans += p * x

    temp = str(ans).split(".")
    if len(temp[1]) != 6:
        temp[1] += "0" * (6 - len(temp[1]))
    print(f"#{case}", end=" ")
    print(".".join(temp))
# 1
# 2
# 0.3 100
# 0.7 1
