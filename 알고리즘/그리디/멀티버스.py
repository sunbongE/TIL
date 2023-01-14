import sys
input = sys.stdin.readline


m, n = map(int, input().split())
d = {}

for _ in range(m):
    li = list(map(int,input().split()))
    k = sorted(list(set(li)))
    # i = {k[i]: i for i in range(len(k))}
    #{0:0, 1:0, 2:0}    
    dic = dict()
    for i in range(len(k)):
        dic[k[i]] = i
    print(dic)