t = int(input())
for case in range(1, 1 + t):
    nums = ""
    ans = 0
    temp = 0
    n = int(input())
    while len(nums) != n:
        nums += "".join(input().split())
    while 1:
        if str(temp) not in nums:
            ans = temp
            break
        temp += 1
    print(f"#{case} {ans}")
