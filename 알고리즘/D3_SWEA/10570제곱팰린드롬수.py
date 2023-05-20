def isPal(str_int):
    if str_int**0.5 == int(str_int**0.5):  # 완전 제곱근?이면
        str_int_sqrt = str(int(str_int**0.5))
        str_int = str(str_int)
        # print(str_int, str_int_sqrt,str_int == str_int[::-1],str_int_sqrt == str_int_sqrt[::-1])
        if str_int != str_int[::-1]:
            return False
        if str_int_sqrt != str_int_sqrt[::-1]:
            return False
        return True
    else:
        return False


ans = []
for case in range(1, 1 + int(input())):
    cnt = 0
    A, B = map(int, input().split())
    for num in range(A, B + 1):
        if isPal(num):
            cnt += 1
    ans.append(cnt)
for i in range(len(ans)):
    print(f"#{i+1} {ans[i]}")
