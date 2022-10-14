import sys
sys.stdin = open('1244.txt')
# 무조건 최대값이 가장 앞으로 오고  #

# def dfs(n):
#     global ans
#     if n == N:
#         # print(ans,int(''.join(map(str,lst))))
#         ans = max(ans, int(''.join(map(str,lst))))
#         return
    
#     for i in range(L-1):
#         for j in range(i+1,L):
#             lst[i],lst[j] = lst[j],lst[i]
#             chk = int(''.join(map(str,lst)))*10+n
#             # print(chk)
#             if chk not in v:
#                 dfs(n+1)
#                 v.append(chk)
#                 # print(v)
#             lst[i],lst[j] = lst[j],lst[i]

# for case in range(1,1+int(input())):
#     st, t = input().split() # 문자형으로 받음
#     N = int(t)
#     lst=[] 
#     v=[]
#     for ch in st:
#         lst.append(int(ch)) #각 문자를 정수형 변환하여 리스트에 추가
#     L = len(lst)
#     ans = 0 
#     dfs(0)

#     print(f'#{case} {ans}')


for tc in range(int(input())+1):
    data, k = input().split()                      
    k = int(k)
    n = len(data)
    # print([data])
    now = set([data])
    # print(now, set(data))
    nxt = set()
    for _ in range(k):
        while now:
            # print(now)
            s = now.pop()
            # print(now,s,type(s))
            s = list(s)
            # print(s)
            for i in range(n-1):
                for j in range(i+1,n):
                    s[i],s[j] = s[j],s[i]
                    nxt.add(''.join(s)) # 중복이 제거돼서 알아서 가지치기가 된다.
                    s[i], s[j] = s[j], s[i]
        now,nxt = nxt,now
        # print(now,nxt)
 
    print('#{} {}'.format(tc,max(map(int,now))))