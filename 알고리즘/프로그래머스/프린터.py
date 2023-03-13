from collections import deque
def solution(priorities, location):
    answer = 0
    

    new_list = [(idx,val) for idx, val in enumerate(priorities)]
    new_list = deque(new_list)

    # print(new_list)
    # 결과 [(0, 1), (1, 1), (2, 9), (3, 1), (4, 1), (5, 1)]
      
    while 1:
        max_=0
        cur = new_list.popleft()
        for i in range(len(new_list)):
            if max_ < new_list[i][1]:
                max_ = new_list[i][1]
        if cur[1] < max_:
            new_list.append(cur)
        else:
            answer += 1
            if cur[0] == location:
                break 
    return answer

print(solution([1, 1, 9, 1, 1, 1],0))

# a=[1, 1, 9, 1, 1, 1]
# new = [(idx,val) for idx, val in enumerate(a)]
# print(new)
