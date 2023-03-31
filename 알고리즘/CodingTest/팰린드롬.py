def is_palindrome(num):
    return str(num) == str(num)[::-1]


def palindrome_sequence(n, m):
    res = []
    for i in range(n, m + 1):
        if is_palindrome(i):
            res.append(i)
    return res


print(palindrome_sequence(1, 100))
