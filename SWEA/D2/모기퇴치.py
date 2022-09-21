# 파리퇴치

# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고,
#  그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
# 다음 N 줄에 걸쳐 N x N 배열이 주어진다
import sys 
sys.stdin = open('모기퇴치.txt','r')

t = int(input())

for case in range(1,1+t):
    n,m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    max_ = 0
    for si in range(n-m+1):
        for sj in range(n-m+1):
            cnt = 0
            for i in range(si,si+m):
                for j in range(sj,sj+m):
                    cnt += mat[i][j]
            if cnt > max_:
                max_ = cnt
    print(f'#{case} {max_}')
