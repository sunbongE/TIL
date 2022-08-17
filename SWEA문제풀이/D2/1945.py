import sys
# sys.stdin = open('t.txt','r')
sys.stdin = open('1945.txt','r')

for t in range(1,1+int(input())):
    N = int(input())
    li =[2,3,5,7,11]
    ans=[0,0,0,0,0]

    for i in range(len(li)):
        while N % li[i] == 0:
            N //= li[i]
            ans[i] += 1
    
    print('#',t,sep='',end=' ')
    print(*ans)