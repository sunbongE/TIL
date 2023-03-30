N, M = map(int, input().split())
tree_H = sorted(map(int, input().split()))

low_H = 0  # 최소 높이
top_H = tree_H[-1]  # 최대 높이

while low_H <= top_H:
    target = (low_H + top_H) // 2
    now_H = sum(max(0, tree - target) for tree in tree_H)
    if now_H < M:
        top_H = target - 1
    elif now_H > M:
        low_H = target + 1
    else:
        print(target)
        break
