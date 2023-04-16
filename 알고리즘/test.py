def dfs(n):
    global ans
    if n == cnt:
        ans = max(ans, int("".join(num_li)))
        return

    for i in range(L - 1):
        for j in range(i + 1, L):
            # 바꾼거 각자리를,...
            num_li[i], num_li[j] = num_li[j], num_li[i]

            # 가지치기...
            # 이미 했던 연산? 결과? 이런걸 또 반복하지 않게 하는것
            check = int("".join(num_li)) * 10 + n  # id
            # check이거 값이 v에 없으면 가자
            if check not in visited:
                dfs(n + 1)
                visited.append(check)

            # 원상복구
            num_li[i], num_li[j] = num_li[j], num_li[i]


for _ in range(int(input())):
    ans = 0
    num, cnt = input().split()
    cnt = int(cnt)
    num_li = [n for n in num]
    visited = []
    L = len(num_li)

    dfs(0)

    print(f"#{_+1} {ans}")

# 32888
# 2 3
# 32888 * 10 + n
