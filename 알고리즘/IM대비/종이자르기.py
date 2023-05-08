w, h = map(int, input().split())
n = int(input())
width = [0, w]
height = [0, h]

for _ in range(n):
    a, b = map(int, input().split())
    if a == 0:
        height.append(b)
    elif a == 1:
        width.append(b)

width.sort()
height.sort()

result = 0
# print(width, height)
for i in range(len(width) - 1):
    for j in range(len(height) - 1):
        x = width[i + 1] - width[i]  # 1 5
        y = height[j + 1] - height[j]  # 6
        print(x, y)
        result = max(result, x * y)

print(result)
# '--------------'

# 2628 종이자르기.py

M, N = map(int, input().split())
width = [0, M]
height = [0, N]

for _ in range(int(input())):
    com, num = map(int, input().split())
    if com == 0:
        height.append(num)
    elif com == 1:
        width.append(num)

ans = 0
width.sort()
height.sort()
# print(width, height)
for i in range(len(width) - 1):
    for j in range(len(height) - 1):
        W = width[i + 1] - width[i]
        H = height[j + 1] - height[j]
        ans = max(ans, W * H)
print(ans)
