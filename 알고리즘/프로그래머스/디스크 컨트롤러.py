import heapq as hp
from collections import deque


def solution(jobs):
    tasks = [[x[1], x[0]] for x in jobs]
    # 실행시간 기준 오름차순 정렬
    tasks = deque(sorted(tasks, key=lambda x: (x[1], x[0])))
    L = len(jobs)
    q = []
    hp.heappush(q, tasks.popleft())

    current_time, total_response_time = 0, 0

    while len(q) > 0:
        run, stop = hp.heappop(q)  # run = 실행식간 stop = 대기시간
        # max(현재시간에서 실행시간 or 대기시간이 긴 경우 + 실행시간)을 더한 current_time은 전체 시간을 나타낸다.
        current_time = max(current_time + run, stop + run)
        # 요청에서 종료까지 시간: 현재 - 대기시간
        # 이미 현재시간에 실행시간을 더한 값이라서 대기시간을 빼면 된다.
        total_response_time += current_time - stop
        while tasks and tasks[0][1] <= current_time:
            # 대기시간이 현재 시간보다 작거나 같은상황
            hp.heappush(q, tasks.popleft())
        if len(tasks) > 0 and len(q) == 0:
            hp.heappush(q, tasks.popleft())
        # if tasks and not q:  # tasks는 있는데 q가 비었으면
        #     # tasks의 값을 q에 삽입
        #     hp.heappush(q, tasks.popleft())
    return total_response_time // L


# print(solution([[0, 3], [1, 9], [2, 6]]))
# print(solution([[7, 8], [3, 5], [8, 6]]))
