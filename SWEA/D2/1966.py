# 주어진 N 길이의 숫자열을 오름차순으로 정렬하여 출력하라.
import sys
sys.stdin = open('1966.txt')
for case in range(int(input())):
    T = int(input())
    nums = list(map(int, input().split()))
    n_nums=[]
    while len(nums) != 0:
        min_=nums.pop(nums.index(min(nums)))
        n_nums.append(min_)
    print(f'#{case+1}', end=' ')
    print(*n_nums)