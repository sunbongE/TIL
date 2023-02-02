
# def f(num):
#     if memo[num]:
#         return memo[num]
#     else:
#         memo[num] = f(num-2) + f(num-3)
#         return memo[num]
    
# tc = int(input())
# for _ in range(tc):
#     n = int(input())
#     if n > 5:
#         memo =[0]*(n+1)
#         memo[1] = memo[2] = memo[3] = 1
#         memo[5] = memo[4] = 2
#         print(f(n))
#     elif n == 4 or n==5:
#         print(2)
#     else:
#         print(1)

# dp풀이
tc = int(input())

for _ in range(tc):
    dp=[0, 1, 1, 1, 2, 2]
    n = int(input())
    if n > 5:
        for i in range(6,n+1):
            dp.append(dp[i-2]+dp[i-3])
        print(dp[n])
    else:
        print(dp[n])
