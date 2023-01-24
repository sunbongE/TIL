import sys
input = sys.stdin.readline
stack=[]
for _ in range(int(input())):
    command = input().split()
    if len(command) == 2:
        stack.append(command[1])
    if command[0] == 'pop':
        if stack:
            pop = stack.pop()
            print(pop)  
        else:
            print(-1)

    if command[0] == 'size':
        print(len(stack))
    
    if command[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)    
    
    if command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)