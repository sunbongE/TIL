for case in range(1, 1 + int(input())):
    ans = 0
    n = int(input())
    li = list(map(int, input().split()))
    avg = sum(li) // n
    for num in li:
        if avg >= num:
            ans += 1
    print(f"#{case}", end=" ")
    print(ans)
