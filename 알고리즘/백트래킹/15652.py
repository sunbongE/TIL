n,m=list(map(int,input().split()))

lst = []

def dfs(s):
    if len(lst) == m:
        print(' '.join(map(str,lst)))
        return
    
    for i in range(s,1+n):
        lst.append(i)
        dfs(i)
        lst.pop()
        
dfs(1)