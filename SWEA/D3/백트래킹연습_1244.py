import sys
sys.stdin = open('1244.txt')

def dfs(n):
    global ans
    if n == N:
        ans = max(ans, int(''.join(lst)) ) # [1,2,3] -> 123
        return
    
    for i in range(len(lst)-1):
        for j in range(i+1,len(lst)):
            lst[i],lst[j] = lst[j],lst[i] # 2130
            # 가지치기 -> 백트래킹
            chk = int(''.join(lst))*10+n # 고유한 값이됨 
            if chk not in v:
                dfs(n+1)
                v.append(chk)
            lst[i],lst[j] = lst[j],lst[i] # 123 

# 입력받기
for case in range(1,1+int(input())):
    st, N = input().split() # 123 1
    N=int(N)
    lst=[]
    v=[]
    for l in st:
        lst.append(l)
    #[1,2,3]
    ans=0
    dfs(0)
    print(f'#{case} {ans}')

 