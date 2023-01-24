n, m, r = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(map(int, input().split())))

for _ in range(r):
    for t in range(min(m, n)//2):
        r, c = t, t
        rows, cols = n-2*t, m-2*t
        tmp = arr[r][c]
        # 왼쪽변
        for cur_r in range(r+1, r+rows):
            original = arr[cur_r][c]
            arr[cur_r][c] = tmp
            tmp = original
        # 아래쪽변
        for cur_c in range(c+1, c+cols):
            original = arr[r+rows-1][cur_c]
            arr[r+rows-1][cur_c] = tmp
            tmp = original
        # 오른쪽변
        for cur_r in range(r+rows-2, r-1, -1):
            original = arr[cur_r][c+cols-1]
            arr[cur_r][c+cols-1] = tmp
            tmp = original
        # 위쪽변
        for cur_c in range(c+cols-2, c-1, -1):
            original = arr[r][cur_c]
            arr[r][cur_c] = tmp
            tmp = original

for r in arr:
    print(" ".join(map(str, r)))
