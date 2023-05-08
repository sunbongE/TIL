N = int(input())
li = [0] + list(map(int, input().split()))
line = [1]
for n in range(2, N + 1):
    if n == 2 and li[n] == 1:  # 2번째사람이 1을 뽑으면
        line.insert(0, n)
    elif n == 2 and li[n] == 0:
        line.append(n)
    else:
        if li[n] != 0:
            line.insert(-li[n], n)
        else:
            line.append(n)
print(*line)
