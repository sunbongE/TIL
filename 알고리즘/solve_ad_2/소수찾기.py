N = int(input())
nums = map(int, input().split())
cnt = 0


def is_prime(num):
    global cnt
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    cnt += 1
    return True


for num in nums:
    is_prime(num)
print(cnt)
