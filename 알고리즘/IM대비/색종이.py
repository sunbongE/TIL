N = int(input())
arr = [[0] * 1001 for _ in range(1001)]

for num in range(1, 1 + N):
    x, y, w, h = list(map(int, input().split()))
    for he in range(y, h + y):
        for wi in range(x, x + w):
            arr[he][wi] = num
for check in range(1, N + 1):
    result = 0
    for ar in arr:
        result += ar.count(check)
    print(result)
