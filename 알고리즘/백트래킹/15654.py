n,m=list(map(int,input().split()))
lst = sorted(list(map(int,input().split())))
l=[]

def dfs(s):
    if len(l) == m:
        print(' '.join(map(str,l)))
        return
    
    for i in range(n):
        if lst[i] not in l:
            l.append(lst[i])
            dfs(lst[i])
            l.pop()
        
dfs(lst[0])