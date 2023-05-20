def Prime(n):
    check = [1] * n
    for i in range(2, int(n**0.5) + 1):
        if check[i] == 1:
            for j in range(i * i, n, i):
                check[j] = 0
    return [n for n in range(2, n) if check[n] == 1]


primes = Prime(1000001)
print(primes)
ans = []
for case in range(1, 1 + int(input())):
    D, A, B = map(int, input().split())
    d = str(D)
    cnt = 0
    for prime in primes:  # 소수들 중에
        if A <= prime <= B:  # 범위내에 있고
            if d in str(prime):  # 특별한 소수인 것
                cnt += 1
    ans.append(cnt)
for i in range(len(ans)):
    print(f"#{i+1} {ans[i]}")
