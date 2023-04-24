T = int(input())

for case in range(1, T + 1):
    N, K = map(int, input().split())
    student = [True] * (N + 1)
    pass_st = list(map(int, input().split()))

    for idx in pass_st:
        student[idx] = False
    print(f"#{case}", end=" ")
    for i in range(1, len(student)):
        if student[i]:
            print(i, end=" ")
    print()
