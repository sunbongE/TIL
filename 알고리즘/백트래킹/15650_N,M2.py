
n,m = list(map(int,input().split()))
lst = []

def f(s):
    if len(lst)==m:
        print(' '.join(map(str, lst)))
        
        return

    for i in range(s,1+n):
        if i not in lst:
            lst.append(i)
            f(i+1)
            lst.pop()
if n == m:
    for a in range(1,1+n):
        print(a,end=' ')
else:            
    f(1)
