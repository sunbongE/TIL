import sys
sys.stdin = open('문서검색.txt','r')

w = input() # aba bab aba
s = input() # aba
cnt = 0

for i in range(0,len(w),len(s)):
    re = w[i:i+len(s)]
    # print(re)
    if s == re:
        cnt+=1
print(cnt)
print(w.count(s))