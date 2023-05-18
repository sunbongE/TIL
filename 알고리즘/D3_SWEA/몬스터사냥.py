for case in range(1, 1 + int(input())):
    D, L, N = map(int, input().split())
    ans = 0
    for n in range(N):
        # print(int(D * (1 + (n * (L * 0.01)))))
        ans += D * (1 + (n * (L * 0.01)))
    ans = int(ans)
    print(f"#{case} {ans}")
