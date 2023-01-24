N,K = map(int,input().split())
li=[]
v = [0] * (N+1)
v[0] = 1
result=[]
for n in range(1,1+N):
    li.append(n)
# print(v)
# print(li)
idx = 0
while 1:
    if sum(v)==N+1:
        break
    idx += 3
    if not v[idx]: #방문안했으면 넣고 방문함
        v[idx]=1
        result.append(li[idx])
    elif v[idx]: # 방문했으면
        while v[idx] == 0:
            if idx > N-1: #인덱스 넘어가면 앞으로 넘기는거
                idx = idx % N-1-1 
            idx += 1 # 다음꺼

    if idx > N-1: #인덱스 넘어가면 앞으로 넘기는거
        idx = idx % N-1-1 
print(result)

