for case in range(1, 1 + int(input())):
    n = int(input())
    li = list(map(str, input().split()))
    n_li = []
    for i in range(n // 2):
        n_li.append(li[i])
        if n % 2 == 1:
            n_li.append(li[i + (n // 2) + 1])
        else:
            n_li.append(li[i + (n // 2)])
    if n % 2 == 1:
        n_li.append(li[n // 2])
    print(f"#{case}", end=" ")
    print(*n_li)
