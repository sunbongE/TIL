# def f(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n == 0:
#         return 0

#     return f(n-1) + f(n-2)
# print(f(int(input())))


# dp 를 이용한 피보나치
def fibo(n):
    f_li = [0, 1, 1]
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    for i in range(3, n + 1):
        f_li.append(f_li[i - 1] + f_li[i - 2])
    return f_li[n]


print(fibo(10))
