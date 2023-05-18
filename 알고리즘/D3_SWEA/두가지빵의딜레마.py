for case in range(1, 1 + int(input())):
    a, b, c = map(int, input().split())
    ans = max(c // a, c // b)
    print(f"#{case} {ans}")
