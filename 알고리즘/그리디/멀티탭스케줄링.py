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

        elif use[i:].index(plug) > far_one:
            far_one = use[i:].index(plug)
            temp = plug
            
    plugs[plugs.index(temp)] = use[i]
    cnt += 1
print(cnt)







#     # 여기부터는 멀티탭에 없는 제품
#     # 멀티탭에 있는 상품중에 빈도수가 낮은 것을 바꿔준다.
#     # 그리고 cnt 1
#     min_=99999
#     for j in multitap:
#         if many_dict[j] < min_:
#             min_ = j
#     multitap.pop(multitap.index(j))
#     multitap.append(li[i])
#     cnt+=1
# print(cnt)

# d={'a':1,'c':3} 
# a=['a','b']

# for i in range(2)   :
#     print(d[a[i]])