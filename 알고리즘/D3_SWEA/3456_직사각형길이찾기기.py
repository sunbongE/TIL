# 3456_직사각형길이찾기기
for case in range(1, 1 + int(input())):
    li = list(map(int, input().split()))
    d = []
    li.sort()
    for l in li:
        if l not in d:
            d.append(l)
        else:
            d.pop()
    print(f"#{case}", end=" ")
    print(*d)
