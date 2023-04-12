# num = input()
# ans = [int(n) for n in num]
# print(sum(ans))

n = int(input())
result = 0
while n:
    result += n % 10
    n //= 10
    print(n, result)
print(result)
