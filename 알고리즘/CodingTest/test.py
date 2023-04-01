def solution(n):
    dic = {
        "0": [2, 2],
        "1": [0, 1],
        "2": [0, 2],
        "3": [0, 2],
        "4": [0, 2],
        "5": [0, 2],
        "6": [1, 2],
        "7": [2, 2],
    }
    answer = []
    if n <= 7:
        answer = dic[str(n)]
    else:
        cnt = n // 7
        target = str(n % 7)

        tem = dic[target]
        if cnt <= 1:
            answer = [tem[0] + 2, tem[1] + 2]
        elif cnt > 1 and target == "0":
            answer = [2 * cnt, 2 * cnt]
        else:
            # answer = [tem[0] + 2 * cnt, tem[1] + (2 * cnt)]
            answer = [tem[0] + (2 * cnt), tem[1] + (2 * cnt)]
            print("target", target)
            print("cnt", cnt)
    return answer


print(solution(29))
print(solution(28))


#
# def solution(n):
#     weekend_counts = [[2, 2], [0, 1], [0, 2], [0, 2], [0, 2], [0, 2], [1, 2], [2, 2]]

#     if n <= 7:
#         answer = weekend_counts[n]
#     else:
#         cnt_weeks = n // 7
#         weekend_index = n % 7

#         weekend_counts_for_weeks = [
#             cnt_weeks + count for count in weekend_counts[weekend_index]
#         ]
#         if cnt_weeks <= 1 and weekend_index != 0:
#             answer = [count + 2 for count in weekend_counts[weekend_index]]
#         else:
#             answer = (
#                 weekend_counts_for_weeks
#                 if weekend_index != 0
#                 else [cnt_weeks * 2, cnt_weeks * 2]
#             )

#     return answer


# def solution(n):
#     weekend_counts = [[2, 2], [0, 1], [0, 2], [0, 2], [0, 2], [0, 2], [1, 2], [2, 2]]
#     answer = []
#     if n <= 7:
#         answer = weekend_counts[n]
#     else:
#         cnt = n // 7
#         target = str(n % 7)

#         tem = weekend_counts[cnt]
#         if cnt <= 1:
#             answer = [tem[0] + 2, tem[1] + 2]
#         elif cnt > 1 and target == "0":
#             answer = [2 * cnt, 2 * cnt]
#         else:
#             # print("?")
#             answer = [tem[0] + 2 * cnt, tem[1] + 2 * cnt]
#             print("target", target)
#             print("cnt", cnt)
#     return answer


# print(solution(29))
# print(solution(28))
