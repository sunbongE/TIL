
n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * n 
temp = []


def dfs(x):
    if len(temp) == m:
        print(*temp)
        return
    remember_me = 0
    for i in range(x,n):
        if  remember_me != nums[i]:
            temp.append(nums[i])
            remember_me = nums[i]
            dfs(x)
            temp.pop()
 
dfs(0)
