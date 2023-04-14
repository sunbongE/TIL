for _ in range(int(input())):
    N = int(input())
    check = [0] * 10  # 0 ~ 9까지 총 10개 생성
    n = 1
    while 1:
        if sum(check) == 10:
            print(f"#{_+1} {result}")
            break
        result = N * n
        for num in str(result):
            if check[int(num)] == 0:
                check[int(num)] = 1
        n += 1
