import sys
sys.stdin = open('성적통계.txt','r')
# 최대 최소 점수차 구하기
# 78 76 30 25 23 
#   2  46 5  2 
# 99 90 70 70 50 25 
#   9  20 0  20 25
# 여기서 최대를 구하는거
#우선 최대최소 구현
t = int(input())
for case in range(1,t+1):
    info = list(map(int, input().split()))
    nums = info[1:] # 수만 따로 분류
    nums.sort(reverse=True)
    max_ = nums[0]
    min_ = nums[-1]
    max_dif = 0
    for i in range(len(nums)-1):# 0~5 
        dif = nums[i] - nums[i+1]
        # print(nums[i],nums[i+1])
        if abs(dif) > max_dif:
            max_dif = abs(dif)
    print(f'Class {case}')
    print(f'Max {max_}, Min {min_}, Largest gap {max_dif}')
