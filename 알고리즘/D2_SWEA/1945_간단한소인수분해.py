targets = [2, 3, 5, 7, 11]
for _ in range(int(input())):
    ans = [0, 0, 0, 0, 0]
    num = int(input())

    while num != 1:
        for idx in range(5):
            if num % targets[idx] == 0:
                num = num // targets[idx]
                ans[idx] += 1
    print(f"#{_+1}", *ans)
