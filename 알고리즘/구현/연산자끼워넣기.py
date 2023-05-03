# 연산자 끼워넣기.
from itertools import permutations

N = int(input())
oper = ["+", "-", "*", "//"]
op_result = []
nums = list(map(int, input().split()))
min_val = float("inf")
max_val = float("-inf")

ops = list(map(int, input().split()))
for i in range(4):  # 연산자 개수별 넣기.
    for _ in range(ops[i]):
        op_result.append(oper[i])
operations = []
for pe in permutations(op_result, N - 1):  # 연산자 조합
    operations.append(pe)

for per in set(operations):
    temp = nums[:]
    for i in range(N - 1):
        if per[i] == "+":
            temp[i + 1] = temp[i] + temp[i + 1]
            temp[i] = 0
        elif per[i] == "-":
            temp[i + 1] = temp[i] - temp[i + 1]
            temp[i] = 0
        elif per[i] == "*":
            temp[i + 1] = temp[i] * temp[i + 1]
            temp[i] = 0
        elif per[i] == "//":
            if temp[i + 1] > 0 and temp[i] < 0:
                temp[i + 1] = -(abs(temp[i]) // temp[i + 1])
            else:
                temp[i + 1] = temp[i] // temp[i + 1]
            temp[i] = 0
    result = temp[-1]
    min_val = min(min_val, result)
    max_val = max(max_val, result)
print(max_val, min_val, sep="\n")
