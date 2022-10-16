# 0으로 시작하지 않는 정수 N이 주어진다. 
# 이때, M을 정수 N의 자릿수라고 했을 때, 다음과 같은 연산을 K번 수행한다.

# 1 ≤ i < j ≤ M인 i와 j를 고른다. 
# 그 다음, i번 위치의 숫자와 j번 위치의 숫자를 바꾼다. 
# 이때, 바꾼 수가 0으로 시작하면 안 된다.

# 위의 연산을 K번 했을 때,
#  나올 수 있는 수의 최댓값을 구하는 프로그램을 작성하시오.
def dfs(n):
    global ans
    if n == K:
        ans = max(ans, int(''.join(lst)))
        return
    
    
    for i in range(L-1):
        for j in range(i+1,L):
            lst[i],lst[j] = lst[j],lst[i]

            chk = int(''.join(lst)) 

            if v.get((chk,n),1):
                v[(chk,n)] = 0
                dfs(n+1)
            lst[i],lst[j] = lst[j],lst[i]



N,K = input().split()
lst, K=list(N), int(K)
v = {}

L = len(lst)
ans = 0
if L <= 1 or (L == 2 and '0' in lst) :
    print(-1)
else:
    dfs(0) 
    print(ans)