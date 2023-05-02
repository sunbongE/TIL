import heapq

T = int(input())

for tc in range(1, T + 1):
    ans = ["#" + str(tc)]
    pq = []
    N = int(input())
    for n in range(N):
        query = list(map(int, input().split()))
        if query[0] == 1:
            heapq.heappush(pq, -query[1])
        else:
            ans.append(str(-heapq.heappop(pq)) if pq else "-1")
    print(" ".join(ans))
