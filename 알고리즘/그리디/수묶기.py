n = int(input())

minus_num = []
plus_num = []
ans = 0
for _ in range(n):
    num = int(input())
    if num > 1:
        plus_num.append(num)
    elif num <= 0:
        minus_num.append(num)
    else:
        ans += num


minus_num.sort() # -55 -2 -1 0 
plus_num.sort(reverse=True) # 4 3 2

# 양수
p_len = len(plus_num)
if p_len % 2 == 0:  # 짝수일 때
    for i in range(0, p_len - 1, 2):
        ans += plus_num[i] * plus_num[i + 1]
else:
    last_num = plus_num.pop()
    for i in range(0, p_len - 1, 2):
        ans += plus_num[i] * plus_num[i + 1]
    ans += last_num

# 음수
n_len = len(minus_num)
if n_len % 2 == 0:  # 짝수일 때
    for i in range(0, n_len - 1, 2):
        ans += minus_num[i] * minus_num[i + 1]
else:
    last_num = minus_num.pop()
    for i in range(0, n_len - 1, 2):
        ans += minus_num[i] * minus_num[i + 1]
    ans += last_num

print(ans)
