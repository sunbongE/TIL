import sys

sys.stdin = open("_민석이의과제체크하기.txt")
# 과제를 제출하지 않은 사람의 오름차순 목록
# 1. t 입력/ n = 학생수 , k = 제출한 수
# 과제를 제출한 사람의 번호 입력
t = int(input())

for case in range(1,t+1):
    re=[]
    li_del = []
    n, k = map(int,input().split())
    li = list(map(int,input().split())) # 2 5 3
    li.sort()
    for num in range(1,1+n): # 1 2 3 4 5
        if num not in li:
            re.append(num)
    print(f'#{case}',end=' ')
    print(*re)
    
    
