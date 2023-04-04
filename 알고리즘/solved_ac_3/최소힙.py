import sys

input = sys.stdin.readline
from heapq import heappop, nsmallest, heappush

hp = []
for _ in range(int(input())):
    com = int(input())
    if com == 0:
        if not hp:
            print(0)
        else:
            result = heappop(hp)
            # nsmallest(len(hp), hp)
            print(result)
    else:
        heappush(hp, com)
