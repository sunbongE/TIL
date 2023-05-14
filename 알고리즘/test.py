from itertools import permutations

for case in range(1, 1 + int(input())):
    N = int(input())
    li = []
    for _ in range(N):
        li.append(input())

    for cnt in range(1, N):
        for per in permutations(li, cnt):
            print(per)
        # break
