for _ in range(int(input())):
    h1, m1, h2, m2 = map(int, input().split())

    H = (h1 + h2) % 12 + (m1 + m2) // 60
    M = (m1 + m2) % 60
    if (h1 + h2) % 12 == 0:  # 1~12시까지있으니까 범위를 맞춘거다.
        H = H + (h1 + h2) // 12
    print(f"#{_+1} {H} {M}")
