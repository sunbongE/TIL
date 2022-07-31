
import sys
sys.stdin = open('1302.txt','r')

N = int(sys.stdin.readline())
dic = {}
for _ in range(N):
    book = sys.stdin.readline().strip()
    dic[book] = dic.get(book,0)+1
#--------------------------------- 풀이 1
# dic = sorted(dic.items())
# max_ = 0
# for k,v in dic:
#     if v > max_:
#         max_ = v
#         result = k
# print(result)
# print(dic)
#--------------------- 풀이 2 
dic = dict(sorted(dic.items()))
max_ = max(dic.values())

for k in dic:
    if dic[k] == max_:
        print(k)
        break