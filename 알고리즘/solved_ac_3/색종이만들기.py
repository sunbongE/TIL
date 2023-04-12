# import sys

# input = sys.stdin.readline

# n = int(input())
# arr = [list(map(int, input().split())) for i in range(n)]

# result = []


# def solution(x, y, n):
#     color = arr[x][y]  # 현 위치의 값을 확인한다.
#     for i in range(x, x + n):
#         for j in range(y, y + n):
#             if color != arr[i][j]:
#                 # 각 사분면의 범위를 재귀호출 매개변수로 넘겨준다.
#                 solution(x, y, n // 2)
#                 solution(x, y + n // 2, n // 2)
#                 solution(x + n // 2, y, n // 2)
#                 solution(x + n // 2, y + n // 2, n // 2)
#                 return
#     if color == 0:
#         result.append(0)
#     else:
#         result.append(1)


# solution(0, 0, n)
# print(result.count(0))
# print(result.count(1))

n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]
result = []


def solution(x, y, n):
    color = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if arr[i][j] != color:
                solution(x, y, n // 2)
                solution(x, y + n // 2, n // 2)
                solution(x + n // 2, y, n // 2)
                solution(x + n // 2, y + n // 2, n // 2)
                return
    if color == 1:
        result.append(1)
    else:
        result.append(0)


solution(0, 0, n)

print(result.count(0))
print(result.count(1))
