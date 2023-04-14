# 입력으로 올 수 있는 수의 범위가 넓기 때문에
# 하나하나 순회한다면 안 풀린다.
# 아마도
# 작은 수, 큰수 찾고 abs()해서 큰 수 만큼 range()해서
# 0부터

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    if nums.count(0):  # 0이 있으면
        print(f"#{_+1} 0 {nums.count(0)}")
    else:
        nums = list(map(abs, nums))
        nums.sort()
        print(f"#{_+1}", nums[0], nums.count(nums[0]))
