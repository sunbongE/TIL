# 입력
T = int(input())
for _ in range(T):
    status = 1
    arr = [list(map(int, input().split())) for _ in range(9)]

    # 1. 가로방향 모두 검사 => set() 이후 len() 길이가 9가 아니면 0 출력
    for ar in arr:
        if len(set(ar)) != 9:
            status = 0
            break

    # 2. 세로방향 검사. => set 후 마찬가지
    for i in range(9):
        temp = []
        for j in range(9):
            temp.append(arr[j][i])
        if len(set(temp)) != 9:
            status = 0
            break

    # 3. 3x3 검사 안에 있는 모든 수를 어떤 변수 리스트에 저장 후 set 마찬가지
    for yy in range(0, 7, 3):
        for xx in range(0, 7, 3):
            temp = []

            for y in range(yy, yy + 3):
                for x in range(xx, xx + 3):
                    temp.append(arr[y][x])
            if len(set(temp)) != 9:
                status = 0
    print(f"#{_+1} {status}")

# 나은 풀이

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for case in range(int(input())):
    ans = 1
    result = []
    for _ in range(9):
        sudoku = list(map(int, input().split()))

        for i in range(9):
            if a[i] not in sudoku:  # 첫번째 조건 가로 줄 숫자 비교
                ans = 0

        result.append(sudoku)

    # 두번째 조건
    for x in range(9):
        b = []
        for y in range(9):
            b.append(result[y][x])
        # print(b)
        for i in range(9):  # 위에 비교문 그대로 가져옴
            if a[i] not in b:
                ans = 0

    # 세번째

    for sj in range(0, 9, 3):  # 0~5
        for sq in range(0, 9, 3):
            c = []
            for j in range(sj, sj + 3):
                for q in range(sq, sq + 3):
                    c.append(result[j][q])

            for i in range(9):  # 위에 비교문 그대로 가져옴
                if a[i] not in c:
                    ans = 0

    print(f"#{case+1} {ans}")
