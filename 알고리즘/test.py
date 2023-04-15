def dfs(n):
    global ans

    if n == cnt:  # cnt만큼 교환했으면 멈춰야함
        ans = max(ans, int("".join(map(str, num_li))))
        return

    for i in range(L - 1):
        for j in range(i + 1, L):
            num_li[i], num_li[j] = num_li[j], num_li[i]

            chk = int("".join(map(str, num_li))) * 10 + n
            if chk not in v:
                dfs(n + 1)
                v.append(chk)
            num_li[i], num_li[j] = num_li[j], num_li[i]


for _ in range(int(input())):
    num, cnt = input().split()
    num_li = [int(nn) for nn in num]
    cnt = int(cnt)
    L = len(num_li)
    ans = 0
    v = []
    dfs(0)

    print(f"#{_+1} {ans}")
