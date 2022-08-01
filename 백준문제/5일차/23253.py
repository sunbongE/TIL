# 자료구조는 정말 최고야..
# 이 문제는 정렬이 가능한지 불가능한지 알아내는 것이 관건
# 예제 입력 2 에서 더미가 [3,5,1], [4,2] 인 상황은 
# 1 2 3 4 5 이런 순서로 뽑아내는 것은 불가능 하다.
# 만약 [5, 3, 1]라면 가능했겠지만.. 그래서 조건문에 
# [3,5,1]와 이 것의 내림차순 정렬된 리스트와 같지 않다면 불가능으로 No를 출력
# 아니면 Yes 출력하면 된다. 

import sys
sys.stdin = open('23253.txt','r')


n, m = map(int, sys.stdin.readline().strip().split())
is_possible = True
for i in range(m):
    cnt = int(sys.stdin.readline().strip())
    nums = list(map(int, sys.stdin.readline().strip().split()))
    if nums != sorted(nums,reverse=True):
         
        is_possible = False
        break
    
if is_possible:
    print('Yes')
else:
    print('No')