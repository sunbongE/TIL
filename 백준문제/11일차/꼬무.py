import sys
sys.stdin = open('꼬무.txt','r')
from pprint import pprint

a,b=map(int,input().split())
a-=1
b-=1
print(abs(a//4-b//4)+abs(a%4-b%4))