import sys
input = sys.stdin.readline

n = int(input())
children = [0] + [*map(int, input().split())]
# print('입력받은 번호',children)
# 0, 5, 2, 4, 1, 3

# 입력받은 번호들 자리수의 인덱스를 구함
nums = [0] * (n+1)
for i in range(1, n+1):
    nums[children[i]] = i
#
# 0, 4, 2, 5, 3, 1
# print(nums)    
count = 1 
max_num = 0

for i in range(1, n):
    if nums[i] < nums[i+1]:
        count += 1
        max_num = max(max_num, count)
    else:
        count = 1

print(n - max_num)