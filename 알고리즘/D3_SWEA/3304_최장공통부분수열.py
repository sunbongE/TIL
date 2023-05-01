# 3304 최장 공통 부분 수열
# 긴 값과 짧은 값을 구분한다.

# 짧은 값을 기준으로 리스트를 하나 생성한다.
# 각 자리수에서 시작한 순회로 얻을 수 있는 공통 부분 수열을
# 리스트에 기록해둔다.

# 탐색이 끝난 후 max(li) 최대 값을 뽑아내면 답이나올것

# lcs_1
# def lcs1(x, y):
#     m, n = len(x), len(y)
#     if m == 0 or n == 0:
#         return 0
#     else:
#         if x[-1] == y[-1]:
#             return lcs(x[: (m - 1)], y[: (n - 1)]) + 1
#         else:
#             return max(lcs(x[:(m)], y[: (n - 1)]), lcs(x[: (m - 1)], y[:(n)]))
# for case in range(1, 1 + int(input())):
#     A, B = input().split()
#     print(lcs1(A, B))


# # lcs_2
def print_matrix(m):
    for i in range(len(m)):
        for j in range(len(m[i])):
            print(m[i][j], end=" ")
        print()


# def lcs2(x, y):
#     x, y = " " + x, " " + y
#     m, n = len(x), len(y)
#     c = [[0] * n for _ in range(m)]

#     for i in range(1, m):
#         for j in range(1, n):
#             if x[i] == y[j]:
#                 c[i][j] = c[i - 1][j - 1] + 1
#             else:
#                 c[i][j] = max(c[i][j - 1], c[i - 1][j])
#     return c[m - 1][n - 1]


# for case in range(1, 1 + int(input())):
#     A, B = input().split()
#     print_matrix(lcs2(A, B))
#     print(f"#{case}", end=" ")
#     print(lcs2(A, B))


# lcs_3
def lcs3(x, y):
    x, y = " " + x, " " + y
    m, n = len(x), len(y)
    result = [[0] * n for _ in range(m)]  # 공통부분수열 기록
    way = [[0] * n for _ in range(m)]  # 최적의 해를 찾는 경로 저장.

    for i in range(1, m):
        for j in range(1, n):
            if x[i] == y[j]:  # 각 자리의 값이 같다면
                result[i][j] = result[i - 1][j - 1] + 1  # 대각선 위 값에 1더한 값
                way[i][j] = 1
            else:
                result[i][j] = max(result[i - 1][j], result[i][j - 1])
                # 어느 것이 큰지 비교해서 어떤 위치의 값이 선택된 것인지 기록한다.
                way[i][j] = 2 if (result[i - 1][j] < result[i][j - 1]) else 3
    return result, way


def get_lcs(i, j, b, x):
    if i == 0 or j == 0:
        return ""
    else:
        if b[i][j] == 1:
            return get_lcs(i - 1, j - 1, b, x) + x[i]
        elif b[i][j] == 2:
            return get_lcs(i, j - 1, b, x)
        elif b[i][j] == 3:
            return get_lcs(i - 1, j, b, x)


for case in range(1, 1 + int(input())):
    A, B = input().split()
    result, way = lcs3(A, B)

    print_matrix(way)
    print(get_lcs(len(A), len(B), way, " " + A))
