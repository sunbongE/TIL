days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())

for i in range(1, T + 1):
    m1, d1, m2, d2 = map(int, input().split())
    # print(days[m1 - 1 : m2 - 1])
    days_passed = sum(days[m1 - 1 : m2 - 1]) + d2 - d1 + 1
    print(f"#{i} {days_passed}")
