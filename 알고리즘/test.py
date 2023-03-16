# #!/bin/python3

# import math
# import os
# import random
# import re
# import sys


# #
# # Complete the 'getFinalString' function below.
# #
# # The function is expected to return a STRING.
# # The function accepts STRING s as parameter.
# #


def getFinalString(s):
    string = "AWAWSS"
    stack = []
    for i in string:
        stack.append(i)
        if stack[-3:] == ["A", "W", "S"]:
            print(stack)
            for j in range(3):
                stack.pop()
        # print(stack)


if __name__ == "__main__":

    s = "AWSAWSAAWSWS"

    result = getFinalString(s)

    # fptr.write(result + "\n")

    # fptr.close()

#!/bin/python3

# import math
# import os
# import random
# import re
# import sys


#
# Complete the 'findRange' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER num as parameter.
#


# def findRange(num):
#     # Write your code here
#     val_max = num
#     val_min = num
#     num = str(num)
#     min_idx = 0
#     target_max = -1
#     target_min = -1
#     check_max = 0
#     check_min = 0
#     for i in range(len(num)):
#         # 최대값 찾기
#         if num[i] != "9" and not check_max:
#             target_max = num[i]
#             # print(target_max)
#             check_max = 1
#         if num[i] != "0" and num[i] != "1" and not check_min:
#             target_min = num[i]
#             min_idx = i
#             check_min = 1
#     if target_max != -1:
#         val_max = num.replace(target_max, "9")

#     if target_min != -1:
#         if min_idx != 0:
#             val_min = num.replace(target_min, "0")
#         else:
#             val_min = num.replace(target_min, "1")

#     # print(val_max)
#     # print(val_min)
#     # print(int(val_max) - int(val_min))
#     return int(val_max) - int(val_min)


# if __name__ == "__main__":

#     num = int(11)

#     result = findRange(num)

# 3번
# import itertools

a = [
    74,
    659,
    931,
    273,
    545,
    879,
    924,
    710,
    441,
    166,
    493,
    43,
    988,
    504,
    328,
    730,
    841,
    613,
    304,
    170,
    710,
    158,
    561,
    934,
    100,
    279,
    817,
    336,
    98,
    827,
    513,
    268,
    811,
    634,
    980,
    150,
    580,
    822,
    968,
    673,
    394,
    337,
    486,
    746,
    229,
    92,
    195,
    358,
    2,
    154,
    709,
    945,
    669,
    491,
    125,
    197,
    531,
    904,
    723,
    667,
    550,
]

k = 22337  # 46

# a = [3, 1, 2, 1]
# k = 4


def maxLength(a, k):
    n = len(a)
    dp = [0] * (k + 1)
    dp[0] = 1  # 초기화

    for i in range(n):
        for j in range(k, -1, -1):
            if j >= a[i] and dp[j - a[i]] > 0:
                dp[j] = 1

    ans = k
    while dp[ans] == 0:
        ans -= 1

    print(ans)
    return ans


# # dp
# def maxLength(a, k):
#     ans = 0
#     dp = [0] * (len(a) + 1)

#     a.sort()
#     # print(a)
#     for i in range(1, len(a) + 1):
#         dp[i] = dp[i - 1] + a[i - 1]
#         if dp[i] <= k:
#             ans = i

#     print(ans)


maxLength(a, k)
