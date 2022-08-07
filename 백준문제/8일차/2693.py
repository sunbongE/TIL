
import sys
sys.stdin = open('n번째큰수.txt','r')
t = int(input())

for _ in range(t):
    li = list(map(int,input().split()))
    li.sort(reverse=True)
    print(li[2])