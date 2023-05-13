def dfs(n, sm):
    global ans
    if sm > K:
        return
    if n == N:
        if K == sm:
            ans += 1
        return
    # 선택
    dfs(n + 1, sm + nums[n])
    # 선택안함
    dfs(n + 1, sm)


for case in range(1, 1 + int(input())):
    N, K = map(int, input().split())
    nums = list(map(int, input().split()))
    ans = 0
    dfs(0, 0)
    print(ans)
