for t in range(10):
    ans = 0
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    for i in range(100):
        prev = 0
        for j in range(100):
            if arr[j][i] == 2 and prev == 1:
                ans += 1
            if arr[j][i] != 0:
                prev = arr[j][i]

    print(f"#{t+1} {ans}")
