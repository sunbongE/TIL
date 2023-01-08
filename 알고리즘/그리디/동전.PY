N,K = map(int,input().split())  
nums = {}
for _ in range(N):
    nums[(int(input()))]=0

for num in sorted(nums.keys(),reverse=True):
    nums[num] = K//num
    if K//num != 0:
        K -= num*(K//num)
print( sum(nums.values()) )
