for case in range(1, 11):
    ans = ""
    L, st = input().split()
    # 연속하는 두 수를 찾으면 바로 없애고 break
    # for 문에서 break 안하면 break=> while 탈출

    while 1:
        for i in range(len(st) - 1):
            if st[i] == st[i + 1]:
                st = st.replace(st[i : i + 2], "", 1)
                break
        else:
            break
    print("#{} {}".format(case, st))
