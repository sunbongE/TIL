import sys

input = sys.stdin.readline

n = int(input())
stack = []
idx = 0
opers_list = []

for _ in range(n):
    target = int(input())

    while (not stack) or (stack[-1] != target):
        if idx >= n:  # 스택에 더이상 추가할 수가 없는데 결과가 안나온 상황
            print("NO")
            exit()
        stack.append(idx + 1)
        idx += 1
        opers_list.append("+")

    stack.pop()
    opers_list.append("-")

print(*opers_list, sep="\n")
# 실행
# 8
# 4
# [1]
# [1, 2]
# [1, 2, 3]
# [1, 2, 3, 4]
# 3
# 6
# [1, 2, 5]
# [1, 2, 5, 6]
# 8
# [1, 2, 5, 7]
# [1, 2, 5, 7, 8]
# 7
# 5
# 2
# 1
