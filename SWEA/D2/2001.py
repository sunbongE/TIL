from pprint import pprint
import sys 
sys.stdin = open('모기퇴치.txt','r')
# N x N 크기의 영역 
# M x M 크기의 파리채
# 2차원 리스트로 순회하여 나오는 값을 전부 더하고
#  result 라는 변수 리스트에 저장 후 최대 값을 추출하면 답이 나옴#

for case in range(int(input())):
    area = []
    result = []
    N, M = map(int,input().split())
    for _ in range(N):
        li = list(map(int, input().split()))
        area.append(li) 
        # 배열 만들었음
    # 이제 2개씩 2줄 순회
    for si in range(N-M+1):
        for sj in range(N-M+1):
            kill = 0
            for i in range(si,si+M):
                for j in range(sj,sj+M):
                    kill += area[i][j]
            #         print(area[i][j])
            # print()
            # print(kill)
            result.append(kill)
    print(f'#{case+1} {max(result)}')
