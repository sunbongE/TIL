for case in range(1, 1 + int(input())):
    ans = 0
    a, b = map(int, input().split())
    if a >= 10 or b >= 10:
        ans = -1
    else:
        ans = a * b
    print(f"#{case} {ans}")
