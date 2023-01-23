import sys
import heapq

input = sys.stdin.readline
N, K = map(int, input().split())

jew = []
for _ in range(N):
    heapq.heappush(jew, list(map(int, input().split())))

bags = []
for _ in range(K):
    bags.append(int(input()))
bags.sort()

answer = 0
tmp_jew = []

for bag in bags:
    while jew and bag >= jew[0][0]:
        heapq.heappush(tmp_jew, -heapq.heappop(jew)[1])
    if tmp_jew:
        answer -= heapq.heappop(tmp_jew)
    elif not jew:
        break
    
print(answer)