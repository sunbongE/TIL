import sys
sys.stdin = open('1244.txt')


def dfs(n): 
    # 1. 종료조건
    global ans
    if n == N:
        ans = max(ans, int(''.join(map(str,lst))))
        # 아래 반복문에서 바꾼 수와 ans에 있던 수 중 큰수가 ans가된다.
        return 
    
    for i in range(L-1):
        for j in range(i+1,L):
            lst[i],lst[j] = lst[j],lst[i] # 앞뒤 숫자를 바꿔줌
            #가지치기
            # 바꾼 리스트모양 수를 고유한 수로 만들어서 
            # 1114 1과 1 을 바꾼 수를 1번 비교하고 또 비교하는건 의미가 없다
            chk = int(''.join(map(str,lst)))*10+n 
            # print(chk) 
            if chk not in v: # 중복을 제거한다.
                dfs(n+1)     # 함수 호출
                v.append(chk)

            lst[i],lst[j] = lst[j],lst[i]
         

#입력받기
for case in range(1,int(input())+1):
    st, N = input().split()
    N = int(N)
    lst = [] # st를 받아서 숫자로 넣을 공간
    v = []    
    for ch in st:
        lst.append(int(ch)) # [1,2,3]
    L = len(lst) # lst 길이
    ans = 0

    dfs(0)

    print(f'#{case} {ans}')
    