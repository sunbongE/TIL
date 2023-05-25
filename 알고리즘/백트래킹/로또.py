def dfs(n, temp):
    # print(n, temp)
    if n >= N:  # 마지막 순번까지 선택해봄.
        if len(temp) == 6:  # 지금 수열이 6개
            if temp not in v:  # 새로운 값이면
                v.append(temp)
        return

    # temp에 추가
    dfs(n + 1, temp + [nums[n]])
    # temp에 빼줌
    dfs(n + 1, temp)


while True:
    nums = list(map(int, input().split()))

    if len(nums) == 1:
        break
    N = nums[0]
    nums = nums[1:]
    v = []
    dfs(0, [])
    for ans in v:
        print(*ans)
    print()
