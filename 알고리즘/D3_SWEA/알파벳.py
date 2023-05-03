# 알파벳
for case in range(1, 1 + int(input())):
    st = input()
    cnt = 0
    tem = 97
    for i in range(len(st)):
        if ord(st[i]) == (tem + i):
            cnt += 1
        else:
            break
    print(f"#{case} {cnt}")
