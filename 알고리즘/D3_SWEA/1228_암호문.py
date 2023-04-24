for case in range(1, 11):
    N = int(input())
    amho = list(input().split())

    com_N = int(input())
    command = list(input().split("I"))
    # 리스트로 묶어야함.
    command = command[1:]
    new_com = []
    # command형식 변환
    for com in command:
        new_com.append(list(com.split()))

    # 순회하면서 명령 실행
    for ncom in new_com:
        for i in range(int(ncom[1])):
            amho.insert(int(ncom[0]), ncom[int(ncom[1]) + 1 - i])
    print("#{} ".format(case), end="")
    print(*amho[:10])
