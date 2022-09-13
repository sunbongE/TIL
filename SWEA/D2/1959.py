import sys
sys.stdin = open("1959.txt")

for _ in range(int(input())):
    N, M = map(int, input().split())
    li_N = list(map(int, input().split()))
    li_M = list(map(int, input().split()))
    result=[]

    if N > M :
        for i in range(N-M+1):
            R=[]
            for x in range(M):
                # print(x+i)
                R.append(li_N[x+i]*li_M[x])
                
            result.append(sum(R))
        print(f'#{_+1} {max(result)}')
    else:
        for i in range(M-N+1):
            R=[]
            for x in range(N):
                # print(x+i)
                R.append(li_N[x]*li_M[x+i])
                
            result.append(sum(R))
        print(f'#{_+1} {max(result)}')

