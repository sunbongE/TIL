for case in range(1, 1 + int(input())):
    ans = "yes"
    arr = []
    check_cnt = 0
    for _ in range(8):
        inp = list(map(str, input()))
        # print(inp, inp.count("O"))
        check_cnt += inp.count("O")
        arr.append(inp)
        if inp.count("O") != 1:
            # print(inp.count("O"))
            ans = "no"
    if ans != "no":  # 8개고 각 행에 룩이 하나씩 있는걸 확인했으면 열을 확인
        new_arr = list(map(list, zip(*arr)))  # 회전시킨거
        for nar in new_arr:
            if nar.count("O") != 1:
                ans = "no"
    print(f"#{case} {ans}")
