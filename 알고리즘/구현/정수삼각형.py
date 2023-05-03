# 정수 삼각형
import sys

input = sys.stdin.readline

n = int(input())
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

if n > 1:
    arr[1][0] += arr[0][0]
    arr[1][1] += arr[0][0]

    for i in range(2, n):
        for j in range(len(arr[i])):
            if j == 0:
                arr[i][j] += arr[i - 1][j]
            elif j == len(arr[i]) - 1:
                arr[i][j] += arr[i - 1][j - 1]
            else:
                arr[i][j] = max(arr[i - 1][j - 1], arr[i - 1][j]) + arr[i][j]
print(max(arr[n - 1]))
