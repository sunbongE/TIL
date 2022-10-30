n,m = map(int,input().split())  
nums = sorted(list(map(int,input().split())))

visited = [False] * n
temp = []

def dfs():
    if len(temp) == m :
        print(*temp)
        return
    pre = 0
    for i in range(n):
        if not visited[i] and pre != nums[i]:
            visited[i] = True 
            temp.append(nums[i])
            pre = nums[i]
            dfs()