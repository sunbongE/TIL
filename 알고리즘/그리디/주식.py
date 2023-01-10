T=int(input())
ss=[]
for _ in range(T):
    buy=[]
    ans=0
    J=int(input())
    nums = list(map(int,input().split()))
    value=0
    max=0
    for i in range(len(nums)-1,-1,-1):
        if(nums[i] > max):
            max = nums[i]
        else:
            value+=max-nums[i]
    print(value)
