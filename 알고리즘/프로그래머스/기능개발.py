import math


def solution(progresses, speeds):
    answer = []
    L = len(speeds)
    idx = -1
    for i in range(L):
        deploy = 1
        cnt = 0
        if i > idx:
            while progresses[i] < 100:
                progresses[i] += speeds[i]
                cnt += 1
            for j in range(i + 1, L):
                if progresses[j] + (speeds[j] * cnt) >= 100:
                    deploy += 1
                    idx = j
                else:
                    break
            answer.append(deploy)
    # print(answer)
    return answer


solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1])
