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

for i in range(len(width) - 1):
    for j in range(len(height) - 1):
        x = width[i + 1] - width[i]
        y = height[j + 1] - height[j]
        result = max(result, x * y)

print(result)
