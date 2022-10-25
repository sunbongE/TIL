n,m = list(map(int,input().split()))

lst = sorted(list(map(int,input().split())))

ans = []

def dfs(s):
    if len(ans) == m:
        print(' '.join(map(str,ans)))
        return
    for i in range(s,n):
        if lst[i] not in ans:
            ans.append(lst[i])
            dfs(i+1)
            ans.pop()   

dfs(0)  