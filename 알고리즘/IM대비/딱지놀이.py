# 1. 별의 개수 다르면 많은게 이김
# 2. 개수가 같으면 동그라미가 같으면 동그라미가 많은게 이김
# 3.

N = int(input())

for _ in range(N):
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    A = sorted(A[1:], reverse=True)
    B = sorted(B[1:], reverse=True)
    for n in range(4, 0, -1):
        a = A.count(n)
        b = B.count(n)
        if a > b:
            print("A")
            break
        elif b > a:
            print("B")
            break
    else:
        print("D")
