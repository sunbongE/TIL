#입력
n,m = list(map(int, input().split()))

lst = sorted(list(map(int, input().split())))
ans = []


def dfs():
    if len(ans) == m:
        print(*ans) 
        return
    for i in range(n):
        
        ans.append(lst[i]) 
        dfs()
        ans.pop()
dfs()