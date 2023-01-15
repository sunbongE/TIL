N = int(input())    
ans=0
li=[]
for _ in range(N):
    li.append(int(input()))


for i in range(len(li)-1):
    if li[N-i-1] <= li[N-i-2]:
        sub=li[N-i-2]+1-li[N-i-1]
        ans += sub
        li[N-i-2] -= sub
print(li)
print(ans)