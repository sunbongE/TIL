from itertools import permutations

for case in range(1, 1 + int(input())):
    num = input()
    ans = "impossible"
    for com in permutations(num, len(num)):
        result = int("".join(com))
        if result > int(num) and result % int(num) == 0:
            ans = "possible"
            break
    print(f"#{case}", end=" ")
    print(ans)
