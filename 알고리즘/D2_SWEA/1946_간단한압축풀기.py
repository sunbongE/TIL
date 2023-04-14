T = int(input())
for tc in range(1, 1 + T):
    n = int(input())
    document = ""
    for _ in range(n):
        word, number = input().split()
        document += word * int(number)

    print("#{}".format(tc))

    for i in range(0, len(document), 10):
        print(document[i : i + 10])
