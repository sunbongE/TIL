from collections import deque


def solution(N, coffee_times):
    L = len(coffee_times)
    coffee_times = [i for i in enumerate(coffee_times, start=1)]
    coffee_times = deque(coffee_times)
    answer = []
    # making=coffee_times[:N]
    # print(making)
    time = 0
    making = []
    while len(answer) != L:
        print(len(answer), L)
        while len(making) != N and coffee_times:
            t = coffee_times.popleft()
            making.append([t, t[1] + time])
        # print(making)
        is_in = 0
        a = 0
        while 1:
            for i in range(len(making)):
                print("시간=>", time)
                print("만드는중=>", making, i)
                if making[i][1] == time:
                    # print("---", making[i][1], time)
                    answer.append(making[i][0][0])  # 답추가
                    #  making에서 뺌
                    print(answer, len(answer))
                    if len(answer) == L:
                        break
                    making.pop(i)
                    break
                is_in += 1
                if is_in == N:
                    a = 1
                    break
            if a:
                break

        while len(making) != N and coffee_times:
            t = coffee_times.popleft()
            making.append([t, t[1] + time])

        time += 1
        # print("시간=>", time)
        # print("만드는중=>", making)
        # print(answer)
        # print(coffee_times)
        # print('시간=>',time)

    return answer


print("답", solution(3, [4, 2, 2, 5, 3]))
