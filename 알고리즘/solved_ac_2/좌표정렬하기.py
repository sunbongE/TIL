n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

li.sort(key=lambda x: (x[0], x[1]))
for n1, n2 in li:
    print(n1, n2)
