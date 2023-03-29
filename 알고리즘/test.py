import sys

input = sys.stdin.readline

n = int(input())
stack = []
idx = 0
opers_list = []

for _ in range(n):
    target = int(input())

    while (not stack) or (stack[-1] != target):
        if idx >= n:
            print("NO")
            exit()
        stack.append(idx + 1)
        idx += 1
        opers_list.append("+")

    stack.pop()
    opers_list.append("-")

print(*opers_list, sep="\n")
