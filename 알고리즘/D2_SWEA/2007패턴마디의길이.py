for _ in range(int(input())):
    check = []
    ans = 0
    st = input()
    for s in st:
        if s not in check:
            check.append(s)
            ans += 1
        else:
            check.pop(check.index(s))
            ans += 1
        if not check:
            ans = ans // 2
            print(f"#{_+1} {ans}")
            break
