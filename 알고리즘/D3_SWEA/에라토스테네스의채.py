import math

# r = int(math.sqrt(1000000))
# print(r)
n = 1000000
arr = [True for _ in range(n + 1)]

for i in range(2, int(math.sqrt(n)) + 1):
    if arr[i] == True:
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1
for ii in range(2, n + 1):
    if arr[ii]:
        print(ii, end=" ")
