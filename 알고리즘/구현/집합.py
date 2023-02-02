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
    
# match case 사용한 풀이
import sys

r = sys.stdin.readline
w = sys.stdout.write

N = int(r())
S = 0

for _ in range(N):
    cmd, *x = r().split()
    if x:
        x = int(x[0])
    match cmd:
        case 'add':
            S |= 1 << x
        case 'remove':
            S &= ~(1 << x)
        case 'check':
            if S & (1 << x):
                w('1\n')
            else:
                w('0\n')
        case 'toggle':
            S ^= 1 << x
        case 'all':
            S = (1 << 21) - 1
        case 'empty':
            S = 0
