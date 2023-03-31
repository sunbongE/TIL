def find_minimum_period(s):
    n = len(s)
    for i in range(1, n + 1):
        if n % i == 0:
            repeated = True
            for j in range(i, n):
                if s[j] != s[j - i]:
                    repeated = False
                    break
            if repeated:
                return i
    return n


print(find_minimum_period("abcabcabd"))
print(find_minimum_period("abababab"))
