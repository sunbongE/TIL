w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

a = (p + t) // w
b = (q + t) // h
# print(a, b)
if a % 2 == 0:
    x = (p + t) % w
else:
    x = w - (p + t) % w

if b % 2 == 0:
    y = (q + t) % h
else:
    y = h - (q + t) % h

print(x, y)
