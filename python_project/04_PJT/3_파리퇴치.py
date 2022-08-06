from pprint import pprint
import sys

# sys.stdin = open("_파리퇴치.txt")
sys.stdin = open("t.txt")
# 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고,
#  그 아래로 각 테스트 케이스가 주어진다.
# 각 테스트 케이스의 첫 번째 줄에 N 과 M 이 주어지고,
# 다음 N 줄에 걸쳐 N x N 배열이 주어진다.
t = int(input())
for case in range(1,1+t):
    n, m = map(int, input().split())  # 5 2
    mat = [list(map(int, input().split())) for _ in range(n)]
# pprint(mat)
    M = [[0]*m for _ in range(m)]
# pprint(M)
    result = []
    # 위 박스
    for i in range(1,n): #1 ~ 4      n =5
        for j in range(1,n): # 1~ 4
            for x in range(m): # m = 2 x= 0, 1
                for y in range(1,m): #
                    M[x][y-1] = mat[i-1][j-1]
                    M[x][y-1]
                    M[x][y-1]
                    M[x][y-1]




                #     M[x-1][y-1] = mat[i-1][j-1] # 0 0 
                #     M[x-1][y] = mat[i-1][j]  #  0 ~ 4 4         
                #     # r = M[0][1]+M[0][0]
                #     M[x][y-1] =  mat[i][j-1]
                #     M[x][y] =  mat[i][j]
                #     r = M[x-1][y-1]+M[x-1][y]+M[x][y-1]+M[x][y]
                #     result.append(r)
                #     print(r)
    # print(result)
    # print(max(result))
    # print(f'#{case} {max(result)}')
# 접근을 못하겠음..