import sys
sys.stdin = open('소가길을건너간이유1.txt','r')
dic={}
n = int(input())    
cnt = 0
for _ in range(n):
    cow, loc = map(int,input().split())
    if cow not in dic:
        dic.setdefault(cow,loc)
    else:
        if loc != dic[cow]:
            cnt += 1
            dic[cow] = loc
print(cnt)