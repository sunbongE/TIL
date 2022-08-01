#우유축제
# 규칙
# 1. 처음은 딸기우유 (0), 2.초코우유(1), 3.바나나(2), 4.딸기0
# 012 012 반복이란말 

n = int(input())

milk = list(map(int,input().split()))
cnt = 0
for i in range(n):
    if cnt % 3 == milk[i]:
        cnt += 1
print(cnt)
