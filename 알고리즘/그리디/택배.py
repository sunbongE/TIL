import sys  

input= sys.stdin.readline

N,C = map(int,input().split())  
M=int(input())  
arr=[]
for _ in range(M):
    arr.append(list(map(int,input().split())))
arr.sort(key= lambda x: x[1])   

box = [C]*(N+1)
ans = 0

for s,e,b in arr:
    
    min_ = C # c개를 옮길수 있다고 가정
    for i in range(s,e) :
        min_ = min(min_,box[i])

    min_ = min(min_, b)
    for i in range(s,e):
        box[i] -= min_
    ans += min_
    
print(ans)