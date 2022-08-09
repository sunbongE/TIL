# N장의 카드에 써져 있는 숫자가 주어졌을 때, 
# M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 구해 출력하시오.
import sys
sys.stdin = open('블랙잭.txt','r')
N, M = map(int,input().split())
#5 21
li = list(map(int, input().split()))
# 5 6 7 8 9
max_ = 0
for i in range(N-2):
    # print(li[i]) # 5 6 7
    for j in range(i+1,N-1):
        # print(li[i],li[j])
        for k in range(j+1,N):
            # print(li[i],li[j],li[k])
            
            ans = li[i] + li[j] + li[k]
            # print(ans, )
            # print('-------------')
            if ans <= M and ans > max_:
                max_ = ans
            if max_ == M:
                break
print(max_)