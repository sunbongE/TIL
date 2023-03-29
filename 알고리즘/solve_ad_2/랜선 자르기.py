# # 가장 최장의 랜선의 길이를 추출하고
# # 그 길이의 반만큼으로 나눈다.
# #
# # 나누는 것은 반복문을 통해 각각 나눈 몫을 더한 값을 저장하는 변수에 담고
# 이분 탐색문제
K, N = map(int, input().split())
lines = []
start = 1
end = 0  # 가장 긴 선의 길이
for _ in range(K):
    line = int(input())
    lines.append(line)
    if line > end:
        end = line

while start <= end:  # end와 start가 같아지는건 조건을 만족하는 최대 랜선길이를 찾았다는것
    mid = (start + end) // 2  # 중간 위치
    cnt = 0  # 랜선 수
    for i in lines:
        cnt += i // mid  # 분할 된 랜선 수

    if cnt >= N:  # 랜선의 개수가 분기점
        start = mid + 1
    else:
        end = mid - 1
print(end)

# 재귀 풀이 더 빠르다..
import sys

input = sys.stdin.readline

k, n = map(int, input().split())
length = [int(input()) for _ in range(k)]


def binary(start, end, arr):
    if start > end:
        return end

    mid = (start + end) // 2
    cnt = 0

    for i in range(k):
        cnt += arr[i] // mid

    if cnt < n:
        return binary(start, mid - 1, arr)
    elif cnt >= n:
        return binary(mid + 1, end, arr)


print(binary(1, max(length), length))
