def isPrime(num):
    m = int(num**0.5)
    n = [True] * (num + 1)
    for i in range(2, m + 1):
        for j in range(i * 2, num, i):
            n[j] = False
    return [i for i in range(2, num) if n[i]]


for case in range(1, 1 + int(input())):
    N = int(input())
    cnt = 0
    li = isPrime(N)
    # print(li)
    L = len(li)
    for i in range(L):
        for j in range(i, L):
            for k in range(j, L):
                if li[i] + li[j] + li[k] == N:
                    # print(li[i],li[j],li[k])
                    cnt += 1
                if li[i] + li[j] + li[k] > N:
                    break
    print(f"#{case} {cnt}")
