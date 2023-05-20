# import math

# # r = int(math.sqrt(1000000))
# # print(r)
# n = 10000000
# arr = [True for _ in range(n + 1)]


# for i in range(2, int(math.sqrt(n)) + 1):
#     if arr[i] == True:
#         j = 2
#         while i * j <= n:
#             arr[i * j] = False
#             j += 1
# for ii in range(2, n + 1):
#     if arr[ii]:
#         print(ii, end=" ")
primes = [2]  # 소수를 저장할 리스트, 초기 소수로 2를 추가합니다.

# 주어진 범위 내에서 소수를 찾습니다.
for num in range(3, int(10000000**0.5) + 1, 2):
    # 홀수만을 대상으로 반복합니다 (짝수는 2로 나누어짐).
    is_prime = True

    # 이전에 찾아낸 소수들로 나누어보고 소수인지 확인합니다.
    for prime in primes:
        if num % prime == 0:
            is_prime = False
            break

    # 소수인 경우 primes 리스트에 추가합니다.
    if is_prime:
        primes.append(num)

print(primes)
