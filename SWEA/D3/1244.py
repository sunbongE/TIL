import sys
sys.stdin = open('1244.txt')
# 무조건 최대값이 가장 앞으로 오고  #

def dfs(n):
    global ans
    if n == N:
        # print(ans,int(''.join(map(str,lst))))
        ans = max(ans, int(''.join(map(str,lst))))
        return
    
    for i in range(L-1):
        for j in range(i+1,L):
            lst[i],lst[j] = lst[j],lst[i]
            chk = int(''.join(lst))*10+n
            # print(chk)
            if chk not in v:
                dfs(n+1)
                v.append(chk)
                # print(v)
            lst[i],lst[j] = lst[j],lst[i]
    

for case in range(1,1+int(input())):
    st, t = input().split() # 문자형으로 받음
    N = int(t)
    lst=[] 
    v=[]
    for ch in st:
        lst.append(ch) #각 문자를 정수형 변환하여 리스트에 추가
    L = len(lst)
    ans = 0 
    dfs(0)

    print(f'#{case} {ans}')