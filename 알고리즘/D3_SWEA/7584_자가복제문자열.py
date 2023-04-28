T = int(input())
answer = []
array = []
for test_case in range(1, T + 1):
    n = int(input()) - 1
    result = 0
    while n >= 0:
        if n % 2 == 1:
            n -= 1
            n //= 2
        elif n % 4 == 0:
            result = 0
            break
        elif n % 2 == 0:
            result = 1
            break

        print("#{} {}".format(test_case, result))
