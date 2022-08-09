import sys
sys.stdin = open('대표값.txt','r')
nums = []
n=5
for _ in range(n):
    num = int(input())
    nums.append(num)
nums.sort()
avg_ = sum(nums)//n
j=nums[round(n/2)]


print(avg_,j,sep='\n')