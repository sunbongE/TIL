from collections import deque
def solution(bridge_length, weight, truck_weights):
    time = 0
    # 0으로 채워진 다리만들고
    bridge_weight=0 # 현재 다리 무게
    truck_weights = deque(truck_weights)
    bridge = deque([0 for _ in range(bridge_length)])
    # print(bridge)
    # while 트럭이 있을 때 까지
    while len(truck_weights) or bridge_weight > 0:
        
        rm = bridge.popleft()
        bridge_weight -= rm

        if len(truck_weights) and (bridge_weight + truck_weights[0]) <= weight:#다리가 버티는 무게라면
            # 다리에 무게를 비교해서 들어올거 같으면 들여보내고
            truck = truck_weights.popleft()
            bridge.append(truck)
            bridge_weight += truck
        else:# 아니면 다리에 있는 차를앞으로 한 칸 이동시키고 0 추가.
            bridge.append(0)

        time +=1
    return time

 
# print(solution(100, 100, [10,10,10,10,10,10,10,10,10,10]))
# print(solution(100, 100, [10]))
print(solution(2, 10, [7,4,5,6]))
# print(solution(10, 12, [4,4,4,2,2,1,1,1,1])) # 26

