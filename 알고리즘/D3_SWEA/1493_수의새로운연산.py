# [풀이 1] dict 사용
# dct = {}
# r_dct = {}
# i, j = 1, 1
# for n in range(1, 50000):  # 10000까지의 숫자를 좌표에 저장할때, 그 4배 크기 삼각형
#     dct[n] = (i, j)
#     r_dct[(i, j)] = n
#     i, j = i - 1, j + 1
#     if i < 1:
#         i, j = j, 1

# T = int(input())
# for test_case in range(1, T + 1):
#     p, q = map(int, input().split())

#     pi, pj = dct[p]  # [1] p, q값의 좌표로 변환
#     qi, qj = dct[q]

#     ans = r_dct[(pi + qi, pj + qj)]  # [2] 좌표를 값으로 변환
#     print(f"#{test_case} {ans}")
##################################################

# [풀이 2] 직접 계산을 사용한 풀이
L = 300
lst = [1] * L
for i in range(2, L):
    lst[i] = lst[i - 1] + i - 1
print(lst)


def pos(n):
    si = 1
    while lst[si] <= n:  # n보다 커질때 멈추고
        si += 1
    si -= 1  # 그 위치에 -1 하면 타겟의 대각선상에 위치한다.
    d = n - lst[si]  # y좌표는 현재 값과 n의 차이가된다.
    return si - d, d + 1


T = int(input())
for test_case in range(1, T + 1):
    p, q = map(int, input().split())

    # [1] 값의 좌표 구하기
    pi, pj = pos(p)
    qi, qj = pos(q)
    si, sj = pi + qi, pj + qj
    ans = lst[si + sj - 1] + sj - 1

    print(f"#{test_case} {ans}")
