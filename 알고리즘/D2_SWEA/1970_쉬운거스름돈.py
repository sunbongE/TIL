money = [
    50000,
    10000,
    5000,
    1000,
    500,
    100,
    50,
    10,
]
for _ in range(int(input())):
    ans = []
    pay = int(input())

    for m in money:
        ans.append(pay // m)
        pay = pay % m
    print(f"#{_+1}")
    print(*ans)
