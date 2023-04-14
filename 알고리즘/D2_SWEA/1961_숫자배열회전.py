for _ in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for __ in range(n)]

    ans_arr = [[] for _ in range(n)]
    # print(arr)
    for ii in range(3):
        change_arr = [[] for _ in range(n)]
        for i in range(n):
            result = ""
            for j in range(n - 1, -1, -1):
                change_arr[i].append(arr[j][i])
                result += str(arr[j][i])
            ans_arr[i].append(result)
        arr = change_arr
    # print(arr)
    print(f"#{_+1}")
    for ans in ans_arr:
        print(*ans)
