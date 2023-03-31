# def solution(mod1, mod2, max_range):
#     answer = [mod1]
#     while 1:
#         if int(max_range) < answer[-1]:
#             break
#         answer.append(mod1 * 2)
#     print(answer)
#     return len(answer)


# # solution(4, 3, 20)
# a = [1, 2, 3]
# b = [2, 3]
# print(set(a) - set(b))
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
