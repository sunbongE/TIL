N = int(input())
nums = list(map(int, input().split()))

nums.sort(reverse=True)
mx = nums[0]
ans = [nums.pop()]

while len(nums) > 0:
    wait = []
    if ans[-1] + 1 == nums[-1]:  # 연속하는 수인지 확인.
        if nums[-1] == mx:
            idx = len(ans) - 1
            while idx >= 0 and ans[idx] == ans[-1]:  # nums넣을 위치 탐색
                idx -= 1
            ans = ans[: idx + 1] + nums + ans[idx + 1 :]
            break
        else:
            while ans[-1] + 1 == nums[-1]:
                wait.append(nums.pop())
    ans.append(nums.pop())
    nums += wait
print(*ans)
