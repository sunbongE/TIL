# 비번찾기
# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())

# dogam = dict()
# for i in range(n):
#     arr, passw = input().split()
#     dogam[arr] = passw

# for j in range(m):
#     print(dogam[input().strip()])

# 해빈이

tc = int(input())
for _ in range(tc):
    ans = 1
    n = int(input())
    box = dict()
    for __ in range(n):
        c, k = input().split()
        box[k] = box.get(k, 0) + 1
    # print(box)
    for d in box:
        ans *= box[d] + 1
    print(ans - 1)
