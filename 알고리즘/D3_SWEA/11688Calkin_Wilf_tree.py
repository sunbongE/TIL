ansList = []
for case in range(1, 1 + int(input())):
    way = input()
    a, b = 1, 1
    for w in way:
        if w == "L":
            b += a
        if w == "R":
            a += b

    ansList.append(f"#{case} {a} {b}")

for ans in ansList:
    print(ans)
