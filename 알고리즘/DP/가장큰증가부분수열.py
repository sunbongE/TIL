
# n=int(input())
# array=list(map(int, input().split()))

# d=[1]*n
# d[0]=array[0]
# for i in range(1,n):
#   for j in range(i):
#     if array[j]<array[i]: # 앞 값이 더 작으면 
#       # 현재 dp값이랑 전값과 현재 arr값 더한 것 중 큰거
#       d[i]=max(d[i], d[j]+array[i]) 
#     else:
#         print(d[i], array[i])
#         d[i]=max(d[i], array[i]) # 
# print(max(d))

n = int(input())
arr = list(map(int, input().split()))
dp = [0] * n
dp[0] =arr[0]
for i in range(n):
    dp[i] = arr[i]
for i in range(1,n):
    for j in range(i):
        if arr[i] > arr[j]:
            # print(arr[i] + dp[j], dp[i])
            # 증가수열이 아닌것을 거르려고 현재 기록된 값과 
            # 반복문을 통해 받아오는 앞의 값과 arr값 합을 비교한것
            # 3 1 ...arr=11 dp[j]=1 dp[i]=14
            # 이런 경우를 걸러주는 역할 
            dp[i] = max(arr[i] + dp[j], dp[i]) 
print(max(dp))
