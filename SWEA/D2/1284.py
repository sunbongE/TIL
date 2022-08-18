import sys
sys.stdin = open('1284.txt','r')

t = int(input())

for i in range(1,t+1):
    A = 0
    B = 0
    P, Q, R, S, W = map(int, input().split())
    A = W*P
    if W <= R:
        B = Q
    else:
        B = Q + abs(R - W)*S
    if A < B:
        print(f'#{i}',A)
    else:
        print(f'#{i}',B)