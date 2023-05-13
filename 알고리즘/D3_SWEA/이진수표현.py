for case in range(1, 1 + int(input())):
    n, m = map(int, input().split())
    result = str(bin(m))
    if "1" * n == result[-n:]:
        ans = "ON"
    else:
        ans = "OFF"
    print(f"#{case} {ans}")
