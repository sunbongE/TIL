# from collections import Counter


# def fac(num):
#     if num == 1:
#         return 1

#     return num * fac(num - 1)


# # print(fac(int(input())))


# result = Counter(str(fac(int(input()))))
# # print(result)
# print(result["0"])
def count_trailing_zeros(n):
    count_2 = 0
    count_5 = 0

    # 1부터 n까지의 숫자에서 2와 5의 개수를 세기
    for i in range(1, n + 1):
        while i % 2 == 0:
            count_2 += 1
            i //= 2
        while i % 5 == 0:
            count_5 += 1
            i //= 5

    # 2와 5의 개수 중 작은 값을 반환
    return min(count_2, count_5)


for i in range(10):
    print(count_trailing_zeros(10 + i))
# 3628800               2
# 39916800              2
# 479001600             2
# 6227020800            2
# 87178291200           2
# 1307674368000         3
# 20922789888000        3
# 355687428096000       3
# 6402373705728000      3
# 121645100408832000    3
