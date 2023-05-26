from math import gcd

N = int(input())
max_num = 0
temp = 0
sub_list = []
for i in range(N):
    t = int(input())
    now_sub = abs(t - temp)
    sub_list += [now_sub]
    temp = t
sub_list = sub_list[1:]

g = sub_list[0]
for i in range(1, len(sub_list)):
    g = gcd(g, sub_list[i])
# print(g)
ans = 0
for j in range(len(sub_list)):
    ans += sub_list[j] // g - 1
print(ans)


# =================================================
def Prime(num):  # 최대 수가 넘어온다. 에라토스테네스의 체
    check = [1] * num
    m = int(num**0.5)
    for i in range(2, m + 1):
        if check[i]:
            for j in range(i * i, num, i):
                check[j] = 0
    return [n for n in range(2, len(check)) if check[n] == 1]


N = int(input())
max_num = 0
temp = 0
sub_list = []
for i in range(N):
    t = int(input())
    now_sub = abs(t - temp)
    sub_list += [now_sub]
    temp = t
    max_num = max(max_num, temp)
prime = Prime(max_num)
# print(prime)
# print(sub_list)
ans = 1e9  # 최대 공약수로 각 차이값을 나눈 몫-1 을 더해준 값.
for i in range(len(prime) - 1, -1, -1):
    result = 0
    for j in range(1, len(sub_list)):
        if sub_list[j] % prime[i] != 0:
            break
        result += sub_list[j] // prime[i] - 1

    if result != 0:
        ans = min(ans, result)

print(ans)
