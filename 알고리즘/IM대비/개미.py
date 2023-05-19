w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

a = (p + t) // w  # 가로 방향으로 이동한 횟수
b = (q + t) // h  # 세로 방향
if a % 2 == 0:  # 이동거리가 짝수면
    x = (p + t) % w
else:  # 이동거리가 홀수면 다시 되돌아 오는 거라서 전체에서 차
    x = w - (p + t) % w

if b % 2 == 0:
    y = (q + t) % h
else:
    y = h - (q + t) % h

print(x, y)
