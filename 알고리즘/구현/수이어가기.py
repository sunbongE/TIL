N = int(input())
ans = 0
result = []
for num in range(N, N // 2, -1):
    li = [N, num]
    temp = li[-1]

    while 1:
        if li[-1] < 0:
            li.pop()
            break
        temp = li[-2] - li[-1]
        li.append(temp)

    if ans < len(li):
        ans = len(li)
        result = li

print(ans)
print(*result)
