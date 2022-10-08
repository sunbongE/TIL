import sys
sys.stdin = open('1234.txt')

for case in range(1,11):
    stack=[]
    leng, li = input().split()
    li = list(li)

    for l in li:
        if not stack:
            stack.append(l)
        else:
            if stack[-1] == l:
                stack.pop()
            else:
                stack.append(l)
    print('#' + str(case), ''.join(stack))