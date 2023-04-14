# N과 M은 3이상 20이하
# 그렇다면 둘중 더 긴 수열이 어떤건지 찾아야한다.
# 긴 수열의 길이를 기준으로 반복문을 돌면서
# 짧은 수열과 모두 곱하고 더한 값을 어떤 변수에 기록해둔다.
# 다음으로 넘어가서 또 기록하는데 더 값이 더 클 때 기록하기위해
# max(ans, temp) 이런 식로 큰것만 기록되게 만든다.

for _ in range(int(input())):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    Long = max(N, M)  # 더 긴 수열 찾음
    short = min(N, M)
    ans = 0
    for i in range(Long - short + 1):
        temp = 0  # 현재 계산된 값 기록 / 변수 초기화
        # print(temp)
        for j in range(short):
            # N이 더 큰경우와 반대의 경우
            if N < M:
                temp += A[j] * B[i + j]  # 곱한거 temp에 계속 더해줌
                # print("A[j]=>", A[j], "B[j+i]=>", B[i + j], temp)
            else:
                temp += B[j] * A[i + j]
        ans = max(ans, temp)
    print(f"#{_+1} {ans}")
