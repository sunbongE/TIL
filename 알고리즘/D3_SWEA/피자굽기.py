for t in range(1, int(input()) + 1):
    # N개의 피자를 동시에 구울 수 있는 화덕
    # M개의 피자를 구워야 함
    N, M = map(int, input().split())
    temp = input().split()
    # 인덱스랑 합쳐서 만들기
    pizza = [(i + 1, int(temp[i])) for i in range(M)]
    print(pizza)
    # 화덕에 들어갈 피자
    pizzas = pizza[:N]
    print(pizzas)
    # 화덕에 못들어간 피자
    pizza = pizza[N:]
    print(pizza)
    # 피자가 1개남을때까지 반복
    while len(pizzas) != 1:
        # 피자를 꺼내서 치즈를 반절로 줄이고
        num, cheese = pizzas.pop(0)
        cheese //= 2
        # 치즈가 있다면 다시 넣는다.
        if cheese:
            pizzas.append((num, cheese))
        # 치즈가 없다면 대기중인 피자를 넣어준다,
        else:
            if pizza:
                pizzas.append(pizza.pop(0))
    print("#{} {}".format(t, pizzas.pop()[0]))
