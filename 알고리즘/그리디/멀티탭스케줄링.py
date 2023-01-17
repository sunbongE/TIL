import sys
input = sys.stdin.readline
N, K = map(int,input().split())  
use = list(map(int,input().split()))
plugs = [] 
cnt=0
for i in range(K):
    if use[i] in plugs:         # 멀티탭에서 이미 사용중인 제품이면 건너뛰기
        continue                
    if len(plugs) != N:         # 멀티탭 공간이 있으면 사용하고 다음으로 넘어감
        plugs.append(use[i])
        continue
    
    far_one = 0
    temp = 0
    for plug in plugs:
        if plug not in use[i:]: # 또 써야하는 제품이 아니라면
            temp = plug         # 그냥 바꿔주면 되니께
            break               # 더이상 플러그를 조회할 필요가 없음
        elif use[i:].index(plug) > far_one: # 
            far_one = use[i:].index(plug)
            temp = plug
    plugs[plugs.index(temp)] = use[i]
    cnt += 1
print(cnt)
