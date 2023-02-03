
def solution(n, lost, reserve):
    # 중복제거
    reserve_only = set(reserve) - set(lost)
    lost_only = set(lost) - set(reserve)
    print('여분',len(reserve_only))
    print('잃어버림',len(lost_only))
    for reserve in reserve_only:
        front = reserve - 1
        back = reserve + 1
        
        if front in lost_only:
            lost_only.remove(front)
        elif back in lost_only:
            lost_only.remove(back)
    return n - len(lost_only)
# # 내풀이.
# def solution(n, lost, reserve):
#     answer = n
#     _reserve = [r for r in reserve if r not in lost]
#     _lost = [l for l in lost if l not in reserve]
#     print('여분',len(_reserve))
#     print(_reserve)
#     print('잃어버림',len(_lost))
#     print(_lost)
#     lost=_lost
#     reserve=_reserve
#     if lost and reserve:
#         lost.sort()
#         for loster in lost:

#             if loster - 1 in reserve:
#                 reserve.remove(loster-1)
#                 continue
#             elif loster + 1 in reserve:
#                 reserve.remove(loster + 1)
#                 continue
#             else: answer -= 1
            
#     elif lost and not reserve:
#         answer -= len(lost)
 
#     return answer


print(solution( 30,
        [1, 2, 7, 9, 10, 11, 12, 14, 15, 16, 18, 20, 21, 24, 25, 27], # 16개
        [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 20, 22, 23, 24, 25, 26, 27, 28]))


