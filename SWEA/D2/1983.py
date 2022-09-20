import sys
sys.stdin = open('1979.txt','r')

G = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']


for case in range(int(input())):
    n,target = input().split()
    n = int(n)
    target = int(target)
    for _ in range(n):
        meq = list(map(int, input().split()))
        m = meq[0]
        e = meq[1]
        q = meq[2]
        total = (m * 0.35) + (e * 0.45) + (q * 0.2)