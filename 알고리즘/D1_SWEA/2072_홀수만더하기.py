for _ in range(int(input())):
    nums = list(map(int, input().split()))
    ans = 0
    for num in nums:
        if num % 2 == 1:
            ans += num
    print(f"#{_+1} {ans}")
