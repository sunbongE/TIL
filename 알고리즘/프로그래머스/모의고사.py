def solution(answers):
    p1 = [1, 2, 3, 4, 5]
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    p_list = [p1, p2, p3]
    dic = {"1": 0, "2": 0, "3": 0}
    ans = []
    for idx in range(len(answers)):
        for p_dix in range(len(p_list)):
            if answers[idx] == p_list[p_dix][idx]:
                dic_idx = str(1 + p_dix)
                dic[dic_idx] += 1
    values = list(dic.values())
    print(values)
    if 1 < values.count(max(values)):
        # print('값이 여러개')
        for _ in range(values.count(max(values))):
            ans.append(1 + values.index(max(values)))
            values.index(max(values))

    else:
        ans.append(1 + values.index(max(values)))
    # print(dic)

    return ans


solution([1, 2, 3, 4, 5])
solution([1, 3, 2, 4, 2])
