# 2805 농작물 수확하기.
# n을 2로 나눈 몫이 농장의 중간 인덱스가 된다.
# print(5 // 2)

for case in range(1, int(input()) + 1):
    n = int(input())
    if n == 1:
        ans = int(input())
        print(f"#{case} {ans}")
        continue

    arr = [list(map(int, input())) for _ in range(n)]
    mid = n // 2
    ans = 0
    ans += sum(arr[mid])
    # print("중간 값 계산", arr[mid])
    # print(arr)
    for i in range(1, 1 + mid):
        dif = i * 2
        ans += sum(arr[mid - i][i : n - i])
        # print(i, "번째 결과", arr[mid - i][i : n - i])
        ans += sum(arr[mid + i][i : n - i])
        # print(i, "번째 결과", arr[mid + i][i : n - i])
    print(f"#{case} {ans}")
