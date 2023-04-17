# 문자형으로 입력받고
# 앞에서부터 순회하여
# 최초의 1이 나오면
# temp변수에 값을 넣고
# 그 다음을 순회하면서

# temp와 값이 다르면 cnt += 1
# 그리고 temp값을 최신화 시킨다.
# 이 과정을 통해 몇번 바꿔야하는지 알 수 있다.

for case in range(1, 1 + int(input())):
    cnt = 0
    st = input()
    temp = -1
    for s in st:
        # print(temp, s)
        if s == "1" and temp == -1:  # 최초 1을 찾으면
            cnt += 1
            temp = s  # temp 값을 현재 값으로 변경
        elif temp != s and temp != -1:  # 값이 다르면 temp 변경
            cnt += 1
            temp = s

    print(f"#{case} {cnt}")
