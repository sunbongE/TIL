from itertools import combinations


def is_valid(num):
    global result
    temp = str(num)
    for idx in range(len(temp) - 1):
        if temp[idx] > temp[idx + 1]:
            return False
    result = max(result, num)


for case in range(1, 1 + int(input())):
    N = int(input())
    nums = list(map(int, input().split()))

    result = 0  # 콤비 돌려서 나온 값중 증가하는 수열형태인 값을 저장.

    for a, b in combinations(nums, 2):
        val = a * b
        is_valid(val)
    if result <= 10:
        result = -1
    print("#{} {}".format(case, result))
