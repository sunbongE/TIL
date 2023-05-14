from itertools import combinations


def check(per):  # a-z까지 있는지 확인
    temp = "".join(per)
    for a in range(97, 123):
        if chr(a) not in temp:
            return False
    return True


for case in range(1, 1 + int(input())):
    ans = 0
    N = int(input())
    li = []
    for _ in range(N):
        li.append(input())

    for cnt in range(1, N + 1):
        for per in combinations(li, cnt):
            if check(per):
                ans += 1
    print(f"#{case} {ans}")
