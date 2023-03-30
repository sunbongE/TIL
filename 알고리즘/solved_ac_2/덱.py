from collections import deque

deck = deque()

for _ in range(int(input())):
    command = input().split()

    if len(command) > 1:
        com = command[0]
        num = command[1]

        if com == "push_front":
            deck.appendleft(num)
        elif com == "push_back":
            deck.append(num)

    else:
        com = command[0]
        if com == "pop_front":
            if deck:
                num = deck.popleft()
                print(num)
            else:
                print(-1)

        elif com == "pop_back":
            if deck:
                num = deck.pop()
                print(num)
            else:
                print(-1)
        elif com == "size":
            print(len(deck))
        elif com == "empty":
            if len(deck) > 0:
                print(0)
            else:
                print(1)
        elif com == "front":
            if deck:
                print(deck[0])
            else:
                print(-1)
        elif com == "back":
            if deck:
                print(deck[-1])
            else:
                print(-1)
