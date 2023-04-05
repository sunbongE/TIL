import sys

input = sys.stdin.readline
import heapq as hp

# 입력값을 음수로 넣고 (heap.heappush)
# 출력할 때  -(출력값) 으로 원래상태로 돌려 출력한다.

heap = []

for _ in range(int(input())):
    in_ = int(input())
    if not heap:
        if in_ == 0:
            print(0)
        else:
            hp.heappush(heap, -in_)
    else:
        if in_ == 0:
            temp = -hp.heappop(heap)
            print(temp)
        else:
            hp.heappush(heap, -in_)
    print(heap)
