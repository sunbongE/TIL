# 평균 소득보다 낮은 사람들이 몇명인지 알아내는 문제임
#전체 케이스 T
import sys
sys.stdin = open('소득불균형.txt','r')
T = int(input())
#각각 2줄로 정수의 개수, 각 사람의 소득
for tc in range(1,T+1):
    cnt = 0 
    N = int(input())
    sod = list(map(int, input().split()))
    avg_sod = sum(sod) // len(sod) # 전체의 합 나누기 인원수의 몫
    for p in sod:
        if p < avg_sod: # 평균 점수보다 작으면 
            cnt += 1
        elif p == avg_sod: # 평균점수와 같으면
            cnt += 1
        
    print(f'#{tc} {cnt}')


