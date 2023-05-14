for t in range(int(input())):
    li = list(map(int, input()))
    ans = 0
    paksu = li[0]  # 박수치는사람
    for i in range(1, len(li)):
        if i > paksu and li[i] != 0:  # 0이 아니고 필요한 박수 인원이 부족하면
            ans += i - paksu  # 이 식으로 계산하면 보충 인원수을 구할수있다.
            paksu += i - paksu  # 필요한 인원 보충
            paksu += li[i]  # 현재 박수치는 사람도 포함시킨다.
        else:
            paksu += li[i]

    print(f"#{t+1} {ans}")
