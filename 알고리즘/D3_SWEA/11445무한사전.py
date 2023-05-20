T = int(input())

result = ""
for num in range(1, T + 1):
    a = input().rstrip()
    b = input().rstrip()
    # a와 b사이에 다른 문자가 있는지 확인하려면 a를 더해서 같은지 보면된다.
    if a + "a" != b:
        result = "Y"
    else:
        result = "N"

    print("#" + str(num), end=" ")
    print(result)
