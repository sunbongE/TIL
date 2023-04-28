# L이상 U이하 운동할것!

for case in range(1, 1 + int(input())):
    L, U, X = map(int, input().split())
    time = 0
    if L > X:
        time = L - X
    elif L < X and X < U:
        time = 0
    else:
        time = -1
    print(f"#{case} {time}")
