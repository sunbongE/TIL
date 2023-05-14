result = []  # 구구단으로 나올 수 있는 값은 다 그냥 저장해버린다.
for i in range(1, 10):
    for j in range(1, 10):
        result.append(i * j)
for case in range(1, 1 + int(input())):
    ans = "Yes"
    num = int(input())
    if num not in result:  # result에 없으면 no
        ans = "No"
    print(f"#{case} {ans}")
