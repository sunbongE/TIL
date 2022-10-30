#입력
n,m = list(map(int, input().split()))

lst = sorted(list(map(int, input().split())))
ans = []


def dfs(x):
    if len(ans) == m:
        print(*ans) 
        return
    for i in range(x,n):
        ans.append(lst[i]) 
        dfs(i)
        ans.pop()
dfs(0)