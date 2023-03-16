import heapq as hp


def solution(operations):
    q = []

    for oper in operations:
        if oper[0] == "I":
            hp.heappush(q, int(oper[2:]))
            q = hp.nsmallest(len(q), q)
        elif oper == "D -1":  # q있는데 이런 명령어 나오면 최소값 지우기.
            if q:
                hp.heappop(q)
                q = hp.nsmallest(len(q), q)
            else:
                pass
        elif oper == "D 1":  # 최대값 삭제
            if q:  # 최대값을 뺄 때 수열이 정렬된 상태가 아니므로 max값을 찾아서 제거
                # hp.nsmallest(len(q), q)
                q.pop()
            else:
                pass
        else:
            pass
        # print(q)
    # q.sort()
    if len(q) > 1:
        max_ = q.pop()  # 최대값
        # print("max==>", max_)
        min_ = hp.heappop(q)  # 최소값 먼저 뽑아보자
        # print("min==>", min_)
        return [max_, min_]
    elif len(q) == 1:
        num = q.pop()
        return [num, num]

    else:
        return [0, 0]


# # print(solution(["I -45", "D 1"]))
# # print(solution(["I 45"]))
# # print(solution(["D 1"]))
# # print(solution(["I -45", "I 11"]))
# # print(
# #     "ans",
# #     solution(
# #         [
# #             "I -45",
# #             "I -45",
# #             "I 653",
# #             "D 1",
# #             "I -642",
# #             "I 45",
# #             "I 97",
# #             "D 1",
# #             "D -1",
# #             "I 333",
# #         ]
# #     ),
# # )
print(
    solution(
        [
            "I 1",
            "I 2",
            "I 3",
            "I 4",
            "I 5",
            "I 6",
            "I 7",
            "I 8",
            "I 9",
            "I 10",
            "D 1",
            "D -1",
            "D 1",
            "D -1",
            "I 1",
            "I 2",
            "I 3",
            "I 4",
            "I 5",
            "I 6",
            "I 7",
            "I 8",
            "I 9",
            "I 10",
            "D 1",
            "D -1",
            "D 1",
            "D -1",
        ]
    )
)
# a = [1, 2, 3, 3, 4, 6, 6, 8, 4, 5, 5, 7, 7]
# print(hp.nsmallest(len(a), a))
