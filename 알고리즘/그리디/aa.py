N, K = map(int,input().split())  

li = list(map(int,input().split()))

multitap = [] 
many_dict=dict()

for k in li: # 각 제품 빈도수를 구함
    many_dict[k]=many_dict.get(k,0)+1
# many_dict = sorted(many_dict.items(), key = lambda item: item[1], reverse = True)
# print(many_dict)
cnt=0
for i in range(K):
    if len(multitap) != N: # 멀티탭 공간이 있으면 사용하고 다음으로 넘어감
        multitap.append(li[i])
        continue
    if li[i] in multitap: # 멀티탭에서 이미 사용중인 제품이면 건너뛰기
        continue
    
    # 여기부터는 멀티탭에 없는 제품
    # 멀티탭에 있는 상품중에 빈도수가 낮은 것을 바꿔준다.
    # 그리고 cnt 1
    min_=99999
    for j in multitap:
        if many_dict[j] < min_:
            min_ = j
    multitap.pop(multitap.index(j))
    multitap.append(li[i])
    cnt+=1
print(cnt)
