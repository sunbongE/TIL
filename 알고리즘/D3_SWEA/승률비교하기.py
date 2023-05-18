ans = []
for _ in range(1, 1 + int(input())):
    A, B, C, D = map(int, input().split())
    result1 = B / A
    result2 = D / C
    if result1 < result2:
        ans.append("ALICE")
    elif result1 == result2:
        ans.append("DRAW")
    else:
        ans.append("BOB")
for i in range(len(ans)):
    print(f"#{i+1} {ans[i]}")
