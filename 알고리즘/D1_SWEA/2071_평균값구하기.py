for _ in range(int(input())):
    nums = list(map(int, input().split()))
    ans = round(sum(nums) / len(nums))

    print(f"#{_+1} {ans}")
