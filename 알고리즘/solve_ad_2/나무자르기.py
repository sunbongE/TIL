import sys

input = sys.stdin.readline
N, M = map(int, input().split())
tree_H = list(map(int, input().split()))

# 일단 ,, 내생각 이분탐색
# 나무중 가장 길이가 작은 값부터 가장 큰 값까지
# 각 수를 빼본다. max(0,(num1-num2)) 0보다 작으면 안댐

# 뺀 값의 전체를 더한 값을 어느 변수에 저장하고 그 변수에 값이 M보다 작다면
# 최대 높이를 줄여야한다.
# 반대로 M보다 크다면 시작 높이를 +=1 해야한다.
# 그럼 어떤 수로 각 나무를 빼줘야 할까
# 이분 탐색문제 같으니까 (최대높이+최소높이)//2 한 값으로 해야할 느낌이다.

# 최저 최고 높이 설정
start = 1
end = max(tree_H)


while start <= end:
    mid = (start + end) // 2
    total_H = 0

    for tree in tree_H:  # 각 트리에 빼기연산
        if tree >= mid:
            total_H += tree - mid

    if total_H >= M:
        start = mid + 1
    else:  # 현재 높이가 더 작으면 최대수를 차감
        start = mid - 1


print(end)
