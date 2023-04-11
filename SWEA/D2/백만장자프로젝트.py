for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    ans = 0
    big_num = 0
    for i in range(n - 1, -1, -1):
        # print(nums[i])
        big_num = max(nums[i], big_num)
        if big_num == nums[i]:
            continue
        else:
            if nums[i] < big_num:
                ans += big_num - nums[i]
    print(f"#{_+1} {ans}")
