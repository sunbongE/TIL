N = int(input())    
li=list(map(int,input().split()))

li.sort()
# 여긴 내코드
# ans = li[0]
# for i in range(1,len(li)):
#     ans += sum(li[:i+1])
# print(ans)
sum_time=0
for i in range(N):
    sum_time += li[i] * (N-i)
    print(li[i], (N-i))
print(sum_time)

# 1 5   5명이 1분을 기다리고
# 2 4   4명이 2분을 기다리고
# 3 3   3명이 3분을 기다리고
# 3 2   2명이 3분을 기다리고
# 4 1   1명이 4분을 기다리는 루트가 가장 짧다.
# 32