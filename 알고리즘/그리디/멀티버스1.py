import sys
input = sys.stdin.readline

m, n = map(int, input().split())
d = {}

for _ in range(m):
    li = list(map(int, input().split()))
    k = sorted(list(set(li)))
    i = {k[i]: i for i in range(len(k))}
    # print(i)
    # print('이게li',li)
    c = str([i[l] for l in li])
    # print(c)
    d[c] = d.get(c, 0) + 1
# print(d)
print(sum(map(lambda x: x * (x - 1) // 2, d.values())))