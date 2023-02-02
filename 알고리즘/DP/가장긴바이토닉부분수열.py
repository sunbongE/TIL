x = int(input())

case = list(map(int, input().split()))
reverse_case = case[::-1]

increase = [1 for i in range(x)] # 가장 긴 증가하는 부분 수열
decrease = [1 for i in range(x)] # 가장 긴 감소하는 부분 수열(reversed)

for i in range(x):
    for j in range(i):
        if case[i] > case[j]:
            increase[i] = max(increase[i], increase[j]+1)
        if reverse_case[i] > reverse_case[j]:
            decrease[i] = max(decrease[i], decrease[j]+1)

result = [0 for i in range(x)]
for i in range(x):
    # print(increase[i], '+' ,decrease[x-i-1] -1)
    result[i] = increase[i] + decrease[x-i-1] -1
    # print('ans',result[i])
print(max(result))

# print(increase)
# print(decrease)
# [1, 2, 2, 1, 3, 3, 4, 5, 2, 1]
# [1, 2, 3, 3, 3, 4, 1, 2, 5, 1]