import sys
sys.stdin = open('0의개수.txt','r')


t = int(input())
for _ in range(t):
    n,m = map(int, input().split())
    li = []
    for num in range(n,m+1):
        li.append(str(num))
    cnt = 0
    for n in li:
        cnt += n.count('0')
         
    print(cnt)