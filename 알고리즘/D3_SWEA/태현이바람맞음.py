for case in range(1, int(input()) + 1):
    ans = 0
    D, H, M = map(int, input().split())

    if D < 11 or (D == 11 and H < 11):
        ans = -1
    else:
        if M < 11:
            H -= 1
            M += 60 - 11
        else:
            M -= 11

        if H < 11:
            D -= 1
            H += 24 - 11
        else:
            H -= 11
        D -= 11
        ans = (D * 24 * 60) + (H * 60) + M

    print(f"#{case} {ans}")
