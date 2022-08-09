import sys
sys.stdin = open('가장많은글자.txt','r')

n=50
string = ''
dic={}
while n:
    try:
        a= input()
        n=-1
        string += a
        
    except EOFError:
        break
for w in string:
    dic[w] = dic.get(w,0)+1

max_ = 0
ans = []
for k,v in dic.items():
    if k != ' ':
        if v >= max_:
            max_ = v
    
for k in dic:
    
    if dic[k] == max_:
        ans.append(k)
ans.sort()
re=''
for o in ans:
    re += o
print(re)