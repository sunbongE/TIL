# 각 명령어? 를 받고 enter,leave 이면 id를 status list에 넣는다.
# 그리고 enter인 경우 닉넴을 사전에 기록해둠
# change도


def solution(record):
    answer = []
    dogam = dict()
    status_li = []
    for r in record:
        info = list(map(str, r.split()))
        if info[0] == "Enter":
            dogam[info[1]] = info[2]
            status_li.append((info[1], "E"))
        elif info[0] == "Change":
            dogam[info[1]] = info[2]
        elif info[0] == "Leave":
            status_li.append((info[1], "L"))
    # print(status_li)
    for i in range(len(status_li)):
        user = dogam[status_li[i][0]]
        if status_li[i][1] == "E":
            com = "님이 들어왔습니다."
        else:
            com = "님이 나갔습니다."
        answer.append(user + com)

    # print(answer)

    return answer


solution(
    [
        "Enter uid1234 Muzi",
        "Enter uid4567 Prodo",
        "Leave uid1234",
        "Enter uid1234 Prodo",
        "Change uid4567 Ryan",
    ]
)
