# N : 손님 수 
# M : 붕어만드는 초
# K : 만든 개수
# 초 단위 0 ~ 11,111
# 모든 손님에 대해 기다리는 시간이 없이 붕어빵을 제공할 수 있으면 “Possible”
# 아니라면 “Impossible”을 출력한다.#

for case in range(int(input())):
    N,M,K = map(int, input().split())
    p = list(map(int,input().split()))
   
    p.sort()
    ans = 'Possible'
    cnt = 0
    for t in p:
        cnt += 1 
        if (t//M)*K < cnt: # 불만족한 조건을 찾아서 끝내는 것이 더 좋다.
            ans = 'Impossible'
            break
    print(f'#{case+1} {ans}')