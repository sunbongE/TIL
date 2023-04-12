import math
import time

start = time.time()
math.factorial(100000)

# for num in range(1, int(input()) + 1): # 1.97534 sec
#     num = str(num)
#     if "3" in num or "6" in num or "9" in num:
#         cnt = 0
#         cnt += num.count("3")
#         cnt += num.count("6")
#         cnt += num.count("9")
#         print("-" * cnt, end=" ")
#     else:
#         print(num, end=" ")

# 다른 풀이
n = int(input())
for i in range(1, n + 1):  # 1.27253 sec
    li = str(i)
    cnt = 0
    for num in li:
        if num in "369":
            cnt += 1
    if cnt == 0:
        print(li, end=" ")
    else:
        print("-" * cnt, end=" ")

end = time.time()

print(f"{end - start:.5f} sec")
