
import sys
sys.stdin = open('대표값.txt','r')


li = []
dic = {}
for _ in range(10):
    num = int(input())
    li.append(num)
    dic[num] = dic.get(num,0)+1
maxi = sorted(dic, key = lambda x:dic[x],reverse= True)

avg_ = sum(li)//10
print(avg_,maxi[0],sep='\n')


