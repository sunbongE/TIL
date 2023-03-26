# 반복으로 한 글자씩 스택으로
# 폭발 문자열의 길이만큼 검색을 해본다.
# 스택[-LEN(폭발):] == 폭발문자열 => POP()
# 남은 스택 출력, 비어있으면 FRULA


word = input()
Boom = list(map(str, input()))
stack = []
# print(Boom)
for w in word:
    stack.append(w)
    if stack[-len(Boom) :] == Boom:
        for _ in range(len(Boom)):
            stack.pop()
# print(stack)
if stack:
    print("".join(stack))
else:
    print("FRULA")
