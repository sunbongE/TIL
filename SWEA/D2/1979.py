from pprint import pprint
import sys
sys.stdin = open('1979.txt','r')
# 첫번째로 가로
# 두번째  세로
# 조건 : 1이면 cnt += 1 하다가 0을 만났는데 cnt가 k 이상이면 ans += 1
# 아니면 cnt = 0
# 끝? #


for case in range(int(input())):
    arr=[]
    N, K = input().split()
    N = int(N)
    K = int(K)
    for _ in range(N):
        li = list(map(int, input().split()))
        arr.append(li)
    
    ans = 0 
    # 가로방향 조회
    for i in range(N):
        cnt = 0
        for j in range(N):
            arr[i][j]
            if arr[i][j] == 1:
                cnt += 1
                
            else:
                if cnt == K:
                    ans += 1
                    cnt = 0
                else:
                    cnt = 0
        if cnt == K:
            ans += 1

        # 세로 방향 조회
    for i in range(N):
        cnt = 0
        for j in range(N):
            arr[j][i]
            if arr[j][i] == 1:
                cnt += 1
                
            else:
                if cnt == K:
                    ans += 1
                    cnt = 0
                else:
                    cnt = 0
        if cnt == K:
            ans += 1
    
    
    print(f'#{case+1} {ans}')

    