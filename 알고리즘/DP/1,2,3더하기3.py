d = [0, 1, 2, 4, 7]
for _ in range(int(input())):
    n = int(input())

    for i in range(len(d), n + 1):
        d.append((d[-3] + d[-2] + d[-1]) % 1000000009)
    print(d)
    print(d[n])
