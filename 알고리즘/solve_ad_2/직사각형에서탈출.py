x, y, w, h = map(int, input().split())

result = []
result.append(abs(x - w))
result.append(abs(y - h))
result.append(min(x, y))
print(min(result))
