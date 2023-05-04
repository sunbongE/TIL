# 4047 영준이의 카드 카운팅

# 출력  S D H C 순

for case in range(1, 1 + int(input())):
    cards = input()
    L = len(cards)
    check = []
    ans = [13, 13, 13, 13]

    for i in range(0, L, 3):
        card = cards[i : i + 3]
        if card not in check:
            check.append(card)
            if card[0] == "S":
                ans[0] -= 1
            elif card[0] == "D":
                ans[1] -= 1
            elif card[0] == "H":
                ans[2] -= 1
            elif card[0] == "C":
                ans[3] -= 1
        else:
            ans = False
            break
    if ans:
        print(f"#{case}", end=" ")
        print(*ans)
    else:
        print(f"#{case} ERROR")
