T = int(input())

for i in range(T):
    N = input().strip()
    n_list = list(N)

    # 최솟값 구하기
    min_list = sorted(n_list)
    if min_list[0] == "0":
        for j in range(1, len(min_list)):
            if min_list[j] != "0":
                min_list[0], min_list[j] = min_list[j], min_list[0]
                break
    min_num = int("".join(min_list))

    # 최댓값 구하기
    max_list = sorted(n_list, reverse=True)
    if max_list[0] == "0":
        for j in range(1, len(max_list)):
            if max_list[j] != "0":
                max_list[0], max_list[j] = max_list[j], max_list[0]
                break
    max_num = int("".join(max_list))

    print("#{} {} {}".format(i + 1, min_num, max_num))
