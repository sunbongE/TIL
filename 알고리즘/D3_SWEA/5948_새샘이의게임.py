from itertools import combinations

for case in range(1, int(input()) + 1):
    nums = list(map(int, input().split()))
    result = []
    for ss in combinations(nums, 3):
        result.append(sum(ss))
    result = sorted(list(set(result)))

    print("#{} {}".format(case, result[-5]))

# 2
# 1 2 3 4 5 6 7
# 5 24 99 76 1 77 6
