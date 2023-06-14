n = int(input())

nums = [int(input()) for _ in range(n)]
nums.sort()
hap = set()
# 두수의 합 모두 구하기.
for i in range(n):
    for j in range(n):
        hap.add((nums[i] + nums[j]))
print(hap)
ans = 0
# x+y = k-z
# 가장 큰 수부터 조회해본다.
flag = False
for i in range(n - 1, -1, -1):
    if flag:
        break
    for j in range(n):
        if nums[i] - nums[j] in hap:
            ans = nums[i]
            flag = True
            break
print(ans)
