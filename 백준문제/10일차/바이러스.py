import sys
from pprint import pprint
sys.stdin = open('바이러스.txt','r')


com = int(input())
li = [[] for _ in range(com+1)]
for _ in range(int(input())):#7
    a,b = map(int,input().split())
    li[a].append(b)
    li[b].append(a)
print(li)

'''
[[],[2,5],[1,3],[2,],[7],[1,2,6],[5],[4]]

1- 2,5
2- 1,3
5- 6
'''