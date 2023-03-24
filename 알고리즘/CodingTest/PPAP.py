# 반복할 작업
# 순회하면서 ppap라는 것이 나오면 p으로 변환한다.
# 반복문이 끝난 후 값이 ppap라면 그래도 출력하고
# 아니면 NP출력한다.
#


w = input()
if w == "P" or w == "PPAP":
    print("PPAP")
else:
    stack = []
    ppap = ["P", "P", "A", "P"]
    for i in w:
        stack.append(i)
        if stack[-4:] == ppap:
            stack.pop()
            stack.pop()
            stack.pop()
    if stack == ppap or stack == ["P"]:
        print("PPAP")
    else:
        print("NP")
