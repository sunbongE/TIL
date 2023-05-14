def get_day_of_week(m, d):
    days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    # 전체 날은 이제까지 왔던 월들의 일수를 더하고 현재 일수 더하고
    # 마지막에 -1 하는 이유는 1월1일을 뺀 것
    total_days = sum(days[: m - 1]) + d - 1
    return (total_days + 4) % 7  # 1월 1일이 금요일이라 4를 더한것.


t = int(input())
for i in range(t):
    m, d = map(int, input().split())
    day_of_week = get_day_of_week(m, d)
    print(f"#{i+1} {day_of_week}")
