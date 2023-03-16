from collections import deque


def solution(prices):
    prices = deque(prices)
    temp = 0
    answer = []
    while prices:
        temp = prices.popleft()
        cnt = 0
        for next in prices:
            cnt += 1
            if temp > next:  # 가격이 떨어지면
                break
        answer.append(cnt)

    # print(answer)
    return answer


# 다른 풀이
def solution(prices):
    answer = [0] * len(prices)
    for i in range(len(prices)):
        for j in range(i + 1, len(prices)):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer


print(solution([1, 2, 3, 2, 3]))
