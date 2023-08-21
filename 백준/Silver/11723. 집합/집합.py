import sys
input = sys.stdin.readline
n = int(input())    
 
S = []
for _ in range(n):
    info = input().split()  
    if info[0] == 'all':
        S=list(range(1,21))
    elif info[0] == 'empty':
        S = []
    else:
        command, x = info
        x = int(x)
        
        if command == 'add':
            if x not in S:
                S.append(x)
        elif command == 'remove':
            if x in S:
                S.remove(x)
        elif command == 'check':
            if x in S:
                print(1)
                
            else:print(0)
        elif command == 'toggle':
            if x in S:
                S.remove(x)
            else: S.append(x)
    
 