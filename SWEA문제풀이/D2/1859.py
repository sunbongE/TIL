import sys
# sys.stdin = open('1859.txt')
sys.stdin = open('t.txt')
# 작거나 같은 값을 추가하고
# 큰 값을 만난 후 작은 값을 만나면 i-1 값을 저장후
# 리스트에 있는 값을 더하고 i-1 값에 리스트 개수만큼 곱하고
# 두 수를 뺀 값을 이득 변수에 += 해줌
# #


for t in range(1,1+int(input())):
    benefit = 0
  
    n = int(input())
    li = list(map(int,input().split()))

    sell = li[-1]
    for i in range(n-2,-1,-1): # 실제로 3~0까지 감 역순으로
        if li[i] >= sell: # 값이 더 크면 바꿈
            sell = li[i]
        benefit += sell - li[i]
    print(f'#{t} {benefit}')
    # print(li, sell)


