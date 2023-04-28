for case in range(1, int(input()) + 1):
    n = int(input())
    days = list(map(int, input().split()))
    class_days = []  # 수업날 인덱스
    for i in range(7):  # 수업이 있는 날 인덱스 탐색
        if days[i] == 1:
            class_days.append(i)

    ans = 1e9
    for day in class_days:
        day_cnt = 0
        class_cnt = 0  # 수업 횟수 저장.
        while class_cnt < n:
            if days[day] == 1:
                class_cnt += 1
            day_cnt += 1
            day = (day + 1) % 7

        ans = min(ans, day_cnt)

    print(ans)


# 3
# 2
# 0 1 0 0 0 0 0
# 100000
# 1 0 0 0 1 0 1
# 1
# 1 0 0 0 0 0 0
