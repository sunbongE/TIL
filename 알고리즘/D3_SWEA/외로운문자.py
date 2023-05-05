# 외로운 문자.

for case in range(1, 1 + int(input())):
    string = list(map(str, input()))
    string.sort()
    ans = []
    for i in range(len(string)):
        if string[i] not in ans:
            ans.append(string[i])
        else:
            ans.pop()
    print(f"#{case}", end=" ")
    if not ans:
        print("Good")
    else:
        print("".join(ans))
