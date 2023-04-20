MOD = 1234567891


# 이항 계수를 구하는 함수
def binomial_coefficient(n, r):
    # n이 r보다 작은 경우, 이항 계수는 0
    if n < r:
        return 0

    # 이항 계수를 저장할 2차원 리스트 초기화
    C = [[0] * (r + 1) for _ in range(n + 1)]

    # 초기값 설정
    for i in range(n + 1):
        C[i][0] = 1
    for j in range(r + 1):
        C[j][j] = 1

    # 이항 계수 구하기
    for i in range(1, n + 1):
        for j in range(1, r + 1):
            C[i][j] = (C[i - 1][j] + C[i - 1][j - 1]) % MOD

    return C[n][r]


# 입력 받기
T = int(input())
for test_case in range(1, T + 1):
    N, R = map(int, input().split())

    # 이항 계수 구하기
    result = binomial_coefficient(N, R)

    # 출력
    print("#{} {}".format(test_case, result))
