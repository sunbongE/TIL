def f(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    elif n == 0:
        return 0

    return f(n-1) + f(n-2)
print(f(int(input())))