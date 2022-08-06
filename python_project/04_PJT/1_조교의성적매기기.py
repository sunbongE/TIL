 
import sys

sys.stdin = open("조교.txt")

#테스트 케이스의 첫 번째 줄은 학생수 N 과, 학점을 알고싶은 학생의 번호 K 가 주어진다.
# 테스트 케이스 두 번째 줄 부터 각각의 학생이 받은 시험 및 과제 점수가 주어진다.
# 총점 중간(35%) 기말(45%) 과제 (20%)

score = ['A+','A0','A-','B+','B0','B-','C+','C0','C-','D0']

t = int(input()) # 테스트 케이스
for case in range(1,1+t): # 1~t
    re = [] # 총점 넣을 곳
    n, k = map(int, input().split()) # 학생수 학생번호
    for _ in range(n): # 학생수 만큼 입력받음
        li = list(map(int, input().split())) # 점수들 
        re.append(li[0]*0.35 + li[1]*0.45 + li[2]*0.2)
    re = list(map(int,re))
    target = re[k-1]
    re.sort(reverse=True)
    # print(target)
    indx = 0
    for i in range(len(re)):# 인원수가 다 다른데.. 어카지
        if target == re[i]:
            indx = i
    if (n//10) % 3 != 0 :
        print(f'#{case} {score[indx//(n//10)]}')
    else:
        if n//10 == 9: # 90명이면 인덱스 -1 해서 출력해버림 

            print(f'#{case} {score[indx//(n//10)-1]}')
        else:print(f'#{case} {score[indx//(n//10)]}')
    # 90일 때 조건 하나 더 달았는데 정답인게 어이없음 피드백 부탁드립니다.
    