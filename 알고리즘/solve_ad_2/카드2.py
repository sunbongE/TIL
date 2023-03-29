from collections import deque

N = int(input())

card = deque([n for n in range(1, N + 1)])

while len(card) != 1:
    # 첫 카드를 버린다
    card.popleft()
    if len(card) > 1:
        # 첫카드 빼서 뒤에 넣음
        tem = card.popleft()
        card.append(tem)
print(*card)
