import sys
sys.stdin = open('카드2.txt','r')

tcase = int(input())
f_num = ['3', '4', '5', '6', '9']
for case in range(1,1+tcase): 
    nums = input()   #1.번호일단 받고
    len_nums = len(nums.replace('-',''))
    if nums[0] in f_num and len_nums == 16:
        print(f'#{case} 1')# 2. 앞글자가 3 4 5 6 9 중 하나인지 확인한다.
    else:
        print(f'#{case} 0')
