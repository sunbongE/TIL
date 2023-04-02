# 팩토리얼


def fac(n):
    if n == 1:  # base condition
        return 1
    return n * fac(n - 1)


# 5 * fac(4) 120
# 4 * fac(3) 24
# 3 * fac(2) 6
# 2 * fac(1) 2
for i in range(10):
    print(fac(10 + i))
# print(fac(500))
