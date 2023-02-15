N, K = map(int, input().split())

nums = list(range(2, N + 1))
cnt = 0
# print(nums)
t = []
while cnt != K:
    P = nums.pop(0)
    # print(P)
    t.append(P)
    cnt += 1
    if cnt == K:
        print(P)
        break
    for num in nums:
        if num % P == 0:
            t.append(num)
            nums.remove(num)
            cnt += 1
            if cnt == K:
                print(num)
                break
# print(t)


def prime_list(n):
    # 에라토스테네스의 체 초기화: n개 요소에 True 설정(소수로 간주)
    sieve = [True] * n

    # n의 최대 약수가 sqrt(n) 이하이므로 i=sqrt(n)까지 검사
    m = int(n**0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:  # i가 소수인 경우
            for j in range(i + i, n, i):  # i이후 i의 배수들을 False 판정
                sieve[j] = False

    # 소수 목록 산출
    # return [i for i in range(2, n) if sieve[i] == True]
    return sieve


prime_list(20)

print(m := int(20**0.5))
