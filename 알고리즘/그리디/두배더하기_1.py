n = int(input())
arr = list(map(int, input().split()))
arr.sort()
cnt = 0
while sum(arr):
    for i in range(n):
        if arr[i] % 2 == 0:
            arr[i] = arr[i] // 2
        else:
            arr[i] -= 1
            # cnt += 1
            break
    cnt += 1
    # print(arr)
    # print(cnt)


print(cnt)
