from heapq import heappush, heapify, heappop


def solution(scoville, K):
    answer = 0
    heapify(scoville)
    # print(scoville)
    while scoville[0] < K:
        if len(scoville) == 1 and scoville[0] < K:
            return -1
        n1 = heappop(scoville)
        n2 = heappop(scoville)

        cur = n1 + (n2 * 2)
        heappush(scoville, cur)
        answer += 1
        # print(scoville)
    return answer


print(solution([1, 10, 3, 9, 2, 12], 7))
# a = [1, 2, 3, 4, 4, 5, -1]
# s = heappop(a)
# print(s)
# print(a)
