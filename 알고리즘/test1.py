N = int(input())

nums = [list(map(int, input().split())) for _ in range(N)]
# print(nums)
for i in range(1, N):
    nums[i][0] = min(nums[i - 1][1], nums[i - 1][2]) + nums[i][0]
    nums[i][1] = min(nums[i - 1][0], nums[i - 1][2]) + nums[i][1]
    nums[i][2] = min(nums[i - 1][1], nums[i - 1][0]) + nums[i][2]
print(min(nums[-1]))
