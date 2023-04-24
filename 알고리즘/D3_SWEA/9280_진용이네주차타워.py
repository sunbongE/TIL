from collections import deque


def parking_func(area_idx, car_idx):
    global money
    money += R_i[area_idx] * W_i[car_idx]


for case in range(1, int(input()) + 1):
    money = 0
    # n 단위 무게당 요금 => [0, 0, 0] 각 자리의 요금으로 생각
    # m 차량의 무게 각 차량의 무게
    n, m = map(int, input().split())
    wait = deque()  # 대기하는 차.
    parking = [0] * n
    R_i = []
    W_i = []
    for _ in range(n):  # 각 자리 요금표 받음.
        R_i.append(int(input()))
    for __ in range(m):
        W_i.append(int(input()))
    for ___ in range(m * 2):
        car_i = int(input())

        # 차량이 들어오면 자리가 있는지 확인한다.
        if car_i > 0:
            for i in range(n):
                # 자리가 있으면 앞에서부터 주차를 한다.
                if parking[i] == 0:
                    parking[i] = car_i
                    parking_func(i, car_i - 1)  # 차 인덱스 맞추려고 1뺌
                    # print(parking, money)
                    break
            # 없다면 기다린다.
            else:
                wait.append(car_i)
                # print(parking, money)

        else:  # 차 나가면
            car_i = abs(car_i)  # 양수로 바꾸고

            if len(wait) > 0:  # 기다리는 차가 있으면 바꿔야함.
                wait_car = wait.popleft()
                parking[parking.index(car_i)] = wait_car
                parking_func(parking.index(wait_car), wait_car - 1)
            else:
                parking[parking.index(car_i)] = 0

    print("#{} {}".format(case, money))
    # 만약 차가 나가면(음수면) 그 수의 양수 인덱스를 찾아서 parking에서 빼고
    # 기다리는 차가 있는지 확인한다.

    # 있으면 popleft() 해서 해당 위치에 넣는다.넣는 위치와 차량정보를 parking이라는 함수에 넘겨준다.

    #
