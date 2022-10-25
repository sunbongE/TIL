n,m = list(map(int, input().split()))
lst = []    

def dfs():
    if len(lst) == m:
        print(' '.join(map(str,lst)))
        return
    for i in  range(1,1+n):
        lst.append(i)
        dfs()
        lst.pop()
dfs()