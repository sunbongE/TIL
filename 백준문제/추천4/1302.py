
import sys
sys.stdin = open('1302.txt','r')

N = int(sys.stdin.readline())
li = []
dic = {}
cnt = 0

for _ in range(N):
    book = sys.stdin.readline().strip()
    dic[book] = dic.get(book,0) + 1
aa = dict(sorted(dic.items())) 
max_ = 0
for i in aa:
    if aa[i] > max_:
        max_ = aa[i]
        maxi=i
print(maxi)
# print(aa)
# print(dic)
    
