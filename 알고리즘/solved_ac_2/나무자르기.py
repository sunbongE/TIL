# 일단 ,, 내생각 이분탐색
# 나무중 가장 길이가 작은 값부터 가장 큰 값까지
# 각 수를 빼본다. max(0,(num1-num2)) 0보다 작으면 안댐

# 뺀 값의 전체를 더한 값을 어느 변수에 저장하고 그 변수에 값이 M보다 작다면
# 최대 높이를 줄여야한다.
# 반대로 M보다 크다면 시작 높이를 +=1 해야한다.
# 그럼 어떤 수로 각 나무를 빼줘야 할까
# 이분 탐색문제 같으니까 (최대높이+최소높이)//2 한 값으로 해야할 느낌이다.
# 최저 최고 높이 설정
import sys

input = sys.stdin.readline
N, M = map(int, input().split())
trees = list(map(int, input().split()))
start = 1
end = max(trees)


while start <= end:  # 적절한 벌목 높이를 찾는 알고리즘
    mid = (start + end) // 2

    total_H = 0  # 벌목된 나무 총합

    for tree in trees:
        total_H += max(0, tree - mid)

    # 반절씩 증가, 감소
    if total_H >= M:
        start = mid + 1
    else:
        end = mid - 1


print(end)
