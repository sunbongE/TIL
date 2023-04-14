# P*W = A사의 요금
# if W < R: Q 기본요금만
# else: Q+S*(W-R)
for _ in range(int(input())):
    A = 0
    B = 0
    P, Q, R, S, W = map(int, input().split())
    A = P * W
    if W < R:
        B = Q
    else:
        B = Q + S * (W - R)
    ans = min(A, B)
    print(f"#{_+1} {ans}")
