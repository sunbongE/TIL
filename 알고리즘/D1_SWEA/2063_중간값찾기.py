n = int(input())

nums = list(map(int, input().split()))

nums.sort()
print(nums[n // 2])
