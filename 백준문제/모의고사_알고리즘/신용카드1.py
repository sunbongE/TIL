import sys
sys.stdin = open('예제입력.txt','r')
 # 룬공식 = 16번째 수 즉 마지막 수 구하기
 
test_case = int(input())

# 한줄입력 공백구분
for case in range(1,1+test_case):
    nums = list(map(int,input().split()))
    even_li = [] # 짝
    odd_li = []  # 홀

    for i in range(len(nums)):
        if (i+1)%2 == 1: #홀수면
            odd_li.append(nums[i]*2)
        elif (i+1)%2 == 0: #짝수면
            even_li.append(nums[i])
    total = sum(odd_li) + sum(even_li)
    # print(total)
    if total % 10 == 0: # 58 % 10 = 8
        print(f'#{case} {0}')
    else:
        print(f'#{case} {10 - total % 10}')
