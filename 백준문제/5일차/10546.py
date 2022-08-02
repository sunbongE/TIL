#배부른 마라토너
import sys 
sys.stdin = open('배부른마라토너.txt','r')

#딕셔너리로 명단 전부 받고 이름이 홀수번있으면
# 사람은 완주를 못한 사람이다.

n = int(sys.stdin.readline())
dic = {}
for _ in range(n+n-1):
    name = sys.stdin.readline().strip()
    dic[name] = dic.get(name,0) + 1

for i in dic:
    if dic[i] %2  == 1:
        print(i)
