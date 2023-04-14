t = int(input())

for _ in range(t):
    ans = 1

    n = int(input())
    for num in range(2, 1 + n):
        if num % 2 == 0:
            ans -= num
        else:
            ans += num

    print(f"#{_+1} {ans}")
