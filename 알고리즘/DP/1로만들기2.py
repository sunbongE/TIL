N = int(input())

result = [[0, []] for _ in range(N + 1)]  # [최솟값, 경로 리스트]
result[1][0] = 0  # 최솟값
result[1][1] = [1]  # 경로를 담을 리스트
# print(result)
for i in range(2, N + 1):

    # f(x-1) + 1
    result[i][0] = result[i - 1][0] + 1
    result[i][1] = result[i - 1][1] + [i]

    # f(x//3) + 1
    if i % 3 == 0 and result[i // 3][0] + 1 < result[i][0]:
        result[i][0] = result[i // 3][0] + 1
        result[i][1] = result[i // 3][1] + [i]

    # f(x//2) + 1
    if i % 2 == 0 and result[i // 2][0] + 1 < result[i][0]:
        result[i][0] = result[i // 2][0] + 1
        result[i][1] = result[i // 2][1] + [i]

print(result[N][0])
# print(result)
for i in result[N][1][::-1]:  # 뒤집은 뒤 출력
    print(i, end=" ")
