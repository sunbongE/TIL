N, M = map(int, input().split())  # N과 M 입력 받기
A = list(map(int, input().split()))  # 수열 A 입력 받기

count = 0  # 경우의 수를 세는 변수 초기화
interval_sum = 0  # 현재 구간의 합을 저장하는 변수 초기화
end = 0  # 끝 포인터 초기화

# 시작 포인터를 차례대로 증가시키며 반복
for start in range(N):
    # 현재 구간의 합이 M과 같거나 커질 때까지 끝 포인터를 증가시킴
    while interval_sum < M and end < N:
        interval_sum += A[end]
        end += 1

    # 현재 구간의 합이 M과 같으면 경우의 수를 증가시킴
    if interval_sum == M:
        count += 1

    # 현재 구간의 합에서 시작 포인터의 값을 빼고 시작 포인터를 증가시킴
    interval_sum -= A[start]
    start += 1

print(count)  # 결과 출력
