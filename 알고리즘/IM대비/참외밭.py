cnt = int(input())
L = []
H = []
info = []
for _ in range(6):
    w, l = map(int, input().split())
    if w in [1, 2]:
        L.append(l)
    else:
        H.append(l)
    info.append([w, l])
target = []
for i in range(6):
    if info[i][0] == info[(i + 2) % 6][0]:  # 2앞에 있는 값의 방향이 같다면
        target.append(info[(i + 1) % 6][1])
total = max(H) * max(L)
print((total - (target[0] * target[1])) * cnt)
