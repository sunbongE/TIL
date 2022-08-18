import sys
sys.stdin = open('1204.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    test_case = int(input())
    score_list = list(map(int,input().split()))
    max_num = 0
    max_idx = 0

    counts = [0] * 101 #0~100 까지 점수 목록을 만듬

    for i in range(1000):#학생수가 1000명이라 1000임
        counts[score_list[i]] += 1 # 1000명 중 i번째 학생의 점수에 접근했고 1 증가 즉 0~100까지 점수에 개수를 구한거임
    # print(counts)

    for i in range(101):
        if counts[i] >= max_num: # 값의 i번째가 이상이면
            max_num = counts[i] # 변수에 할당 즉, 비교하면서 가장 큰 값이 변수에 들어오게됨
            max_idx = i # 큰값을 찾으면 그 값의 인덱스를 기록해둔거임
    print('#{} {}'.format(tc, max_idx))