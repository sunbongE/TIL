for _ in range(int(input())):
    n = int(input())
    triangle = [[] for _ in range(n + 1)]  # 삼각형을 담을 리스트

    for i in range(1, n + 1):
        if i == 1:  # 첫번째는 그냥 1 만 넣음
            triangle[1].append(1)
        elif i == 2:  # 두번째는 1을 두개 넣음
            triangle[2].append(1)
            triangle[2].append(1)
        else:  # 이후로는
            for j in range(i):  # i만큼 즉, 몇번째 줄인가 만큼 반복해서 값을 채울거다.
                if j == 0 or j == i - 1:  # 처음과 끝은 항상 1이다.
                    triangle[i].append(1)
                else:  # 처음과 끝이 아니면!
                    # 현재 내 위치의 값 = 전 리스트의 내위치 + 전 리스트의 내위치-1
                    val = triangle[i - 1][j] + triangle[i - 1][j - 1]
                    triangle[i].append(val)

    # 답 출력 형식.. [[], [1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1]]
    # 0번째 빼고 1부터 마지막까지 한줄에 한 리스트씩 출력
    print(f"#{_+1}")
    for idx in range(1, n + 1):
        print(*triangle[idx])  # 리스트에 * 이런 별표를 붙이면 리스트가 풀려서 출력된다. 즉, [1,2] => 1,2 요러케


# 더 깔끔한 풀이
for case in range(int(input())):
    n = int(input())
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    arr[1][1] = 1
    for y in range(2, n + 1):
        for x in range(1, y + 1):
            # pass
            arr[y][x] = arr[y - 1][x - 1] + arr[y - 1][x]

    print(f"#{case+1}")
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(arr[i][j], end=" ")
        print()
