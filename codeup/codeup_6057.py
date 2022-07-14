a, b = map(int, input().split())

a = bool(a)
b = bool(b)

print((a and b) or (not a and not b))