from itertools import combinations

for case in range(1, int(input()) + 1):
    # 리스트로 전환
    nums = list(map(str, input()))
    # print(nums)
    idx_list = [i for i in range(len(nums))]
    # 인덱스 별로 전부 바꿔 max,min 찾기.
    # 초기화는 변경하기 전 값으로.
    max_num = min_num = int("".join(nums))

    # combinations 수의 조합으로 변경
    for combi in combinations(idx_list, 2):
        i, j = combi

        nums[i], nums[j] = nums[j], nums[i]
        # 첫자리가 0이면 돌려놓기.
        if nums[0] == "0":
            nums[i], nums[j] = nums[j], nums[i]
            continue
        if int("".join(nums)) < min_num:
            min_num = int("".join(nums))
        if int("".join(nums)) > max_num:
            max_num = int("".join(nums))
        # 끝나면 돌려놔야함.
        nums[i], nums[j] = nums[j], nums[i]
    print("#{} {} {}".format(case, min_num, max_num))
