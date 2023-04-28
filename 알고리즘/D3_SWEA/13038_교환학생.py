def solve(N, A):
    ClassDayList = []  #  수업이 있는 날의 인덱스 기록
    for i in range(len(A)):  # 수업있는 날은 리스트에 추가
        if A[i] == 1:
            ClassDayList.append(i)
    ans = 1e9

    for day in ClassDayList:  # 수업있는 날부터터 돌면서
        day_cnt = 0  # 머무는 일수
        class_cnt = 0  # 수업 횟수
        while class_cnt < N:  # 목표 수업 수보다 적을때
            if A[day] == 1:  # 수업날이면 +1
                class_cnt += 1
            day_cnt += 1  # 한번 돌면 하루 지난거임
            day = (day + 1) % 7  # day 0~6까지 7개 인덱스임
        ans = min(ans, day_cnt)
    return ans


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    A = list(map(int, input().split()))
    ans = solve(N, A)
    print(f"#{test_case} {ans}")

# ans = min(ans, dayCnt) 수업이 있는 각 요일에서 시작해서 최소 머물 일수를 구한다.
# 아래 예시를 해결할 수 있다. 토 일은 붙어있다.
# 1
# 2
# 1 0 0 0 0 0 1
# 1 2
