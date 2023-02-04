n=int(input())
distance = list(map(int,input().split()))
city = list(map(int,input().split()))
# total_distance = sum(distance)
# pay = 0
# min_ = city[0]*total_distance


# for i in range(1,n):
#     total_distance -= distance[i-1]
#     temp=0
#     temp += total_distance * city[i]
#     for j in range(i):
#         temp += (distance[j]*city[j])
#     if temp < min_:
#         min_ = temp
    
# print(min_)

res = 0
m = city[0]
for i in range(n-1):
    if city[i] < m:
        m = city[i]
    res += m*distance[i]
print(res)