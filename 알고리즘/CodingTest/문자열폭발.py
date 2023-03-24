word = input()
Boom = list(map(str, input()))
stack = []
# print(Boom)
for w in word:
    stack.append(w)
    if stack[-len(Boom) :] == Boom:
        for _ in range(len(Boom)):
            stack.pop()
if stack:
    print("".join(stack))
else:
    print("FRULA")
