n,m = map(int,input().split())
li=list(map(int,input().split()))

for _ in range(m):
    li.sort()
    # print(li)
    re = li[0] + li[1]
    li[0] = re
    li[1] = re
print(sum(li))
# 힙을 이용한 풀이
# import heapq
# n, m = map(int, input().split())
# cards = list(map(int, input().split()))
# heapq.heapify(cards)

# for i in range(m):
#     a = heapq.heappop(cards)
#     b = heapq.heappop(cards)

#     heapq.heappush(cards, a + b)
#     heapq.heappush(cards, a + b)

# print(sum(cards))