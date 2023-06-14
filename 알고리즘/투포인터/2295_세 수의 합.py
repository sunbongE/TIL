N = int(input())
arr = [int(input()) for _ in range(N)]
arr.sort()
ans = 0
# 두 수의 합으로 나올 수 있는 모든 경우를 계산한 값
# {4, 5, 6, 7, 8, 36, 10, 12, 13, 15, 20, 21, 23, 28}
arr_sum = set()
for i in arr:
    for j in arr:
        arr_sum.add(i + j)
flag = False
for i in range(N - 1, -1, -1):
    if flag:
        break
    for j in range(N):
        if arr[i] - arr[j] in arr_sum:
            ans = arr[i]
            flag = True
            break

print(ans)


# 5 => n
# 2
# 3
# 5
# 10
# 18
