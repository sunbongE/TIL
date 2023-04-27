for case in range(1, int(input()) + 1):
    n = int(input())
    li = list(map(int, input().split()))
    cnt = 0
    while n:
        for i in li:
            if i == 1:
                cnt += 1
                n -= 1
    print(cnt)
