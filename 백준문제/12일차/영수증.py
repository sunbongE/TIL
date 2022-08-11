import sys
sys.stdin = open('영수증.txt','r')
total = 0
X = int(input())
for _ in range(int(input())):
    price, cnt = map(int,input().split())
    total += (price*cnt)
if X == total:
    print('Yes')
else:
    print('No')