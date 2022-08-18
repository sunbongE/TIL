import sys
sys.stdin = open('1976.txt','r')


t = int(input())

for i in range(1,t+1):
    H1, M1, H2, M2 = map(int, input().split())
    H3 = H1 + H2
    M3 = M1 + M2
    if H3 > 12:
        H3 = H3 - 12
    if M3 > 60:
        M3 = M3 - 60
        H3 += 1
    print(f'#{i}',H3,M3)