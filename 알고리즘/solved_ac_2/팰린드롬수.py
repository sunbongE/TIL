while 1:
    is_pal = "yes"
    target = input()
    if target == "0":
        break
    L = len(target)
    for i in range(L):
        if is_pal == "no":
            break
        else:
            for j in range(0, L // 2):
                # print(target[j], target[L - j - 1])
                if target[j] != target[L - j - 1]:
                    is_pal = "no"

                    break

    print(is_pal)
