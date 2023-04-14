for _ in range(int(input())):
    ans = 0
    nums = list(map(int, input().split()))

    nums.sort()
    target = nums[1:9]
    ans = round(sum(target) / 8)
    print(f"#{_+1} {ans}")
