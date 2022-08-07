import sys
sys.stdin = open('붕어빵.txt','r')
n, m = map(int, input().split())

for _ in range(n):
    bung = input()
    print(bung[::-1])