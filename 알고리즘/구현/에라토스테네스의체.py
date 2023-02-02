N,K = map(int,input().split())  

nums = list(range(2,N+1))
cnt = 0
# print(nums)
t=[]
while cnt != K:
    P = nums.pop(0)
    # print(P)
    t.append(P)
    cnt += 1
    if cnt == K :
        print(P)
        break
    for num in nums:
        if num % P == 0:
            t.append(num)
            nums.remove(num)
            cnt += 1
            if cnt == K:
                print(num)
                break
# print(t)