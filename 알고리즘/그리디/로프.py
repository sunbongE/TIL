import sys
input = sys.stdin.readline
nums=[]
N=int(input())
for _ in range(N):
    nums.append(int(input()))

nums.sort(reverse=True) 
new_li=[]
for c in range(1,len(nums)+1):
    new_li.append(c*nums[c-1])
print(max(new_li))