for _ in range(int(input())):
    n1, n2 = list(map(int, input().split()))
    op = ""
    if n1 == n2:
        op = "="
    elif n1 < n2:
        op = "<"
    else:
        op = ">"
    print(f"#{_+1} {op}")
