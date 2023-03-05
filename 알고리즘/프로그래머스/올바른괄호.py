def solution(s):
    answer = True
    temp = []
    for i in range(len(s)):
        if s[i] == "(":
            temp.append(s[i])
        else:
            if s[i] == ")" and temp:
                temp.pop()
            elif not temp:
                temp.append(s[i])
        # print(temp)
    if temp:
        answer = False
    return answer


print(solution("(())()"))
print("--------------")
print(solution("(()("))
