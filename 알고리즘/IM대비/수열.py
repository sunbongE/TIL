N = int(input())
nums = list(map(int, input().split()))
down_dp = [1] * N
up_dp = [1] * N
for i in range(1, N):
    if nums[i] >= nums[i - 1]:
        up_dp[i] = up_dp[i - 1] + 1
    if nums[i] <= nums[i - 1]:
        down_dp[i] = down_dp[i - 1] + 1
print(max(max(up_dp), max(down_dp)))
