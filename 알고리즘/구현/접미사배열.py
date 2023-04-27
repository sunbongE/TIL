st = input()
L = len(st)
li = []
for i in range(L):
    li.append(st[i:])
print(*sorted(li), sep="\n")
