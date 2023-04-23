n = int(input())

nums = list(map(int, input().split()))

dp = [1] * n
dp[0] = nums[0]

for i in range(1, n):
    for j in range(i):
        # 현재 선택된 값이 더 크면 증가인것
        if nums[i] > nums[j]:
            # print(nums[i], nums[j])
            # 현재 기록된 dp값과 탐색한 dp값 + 내 값을 한 것 중에 큰 값
            dp[i] = max(dp[i], dp[j] + nums[i])
            # print(dp)
        # 증간 경우가 아닌 것.
        else:
            # 내 값과 현재 기록된 값 중 큰 값을 가져야한다.
            dp[i] = max(dp[i], nums[i])
print(max(dp))
