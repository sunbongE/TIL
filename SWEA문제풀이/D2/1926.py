import sys
sys.stdin = open('1926.txt','r')


n=int(input()) # 100

for i in range(1,n+1):
    cnt = 0
    s = str(i)
    for j in s:
        
        if j == '3' or j == '6' or j == '9':
            cnt += 1       
            
    if cnt == 0:
        print(i,end=' ')
    else:
        print("-"*cnt, end=' ',sep='')