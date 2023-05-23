def dfs(n, sm, cnt):  # 선택한 상황에서 S가 된것인지 확인해야한다.
    global ans
    if n == N:
        if sm == S and cnt:
            ans += 1
        return
    dfs(n + 1, sm + nums[n], cnt + 1)
    dfs(n + 1, sm, cnt)


ans = 0
N, S = map(int, input().split())
nums = list(map(int, input().split()))
# n,합,선택여부
dfs(0, 0, 0)
print(ans)
