import sys
sys.stdin = open('1984.txt','r')

for case in range(int(input())):
    a = list(map(int, input().split()))
    a.sort()
    a.pop()
    a.sort(reverse=True)
    a.pop()
    avg = sum(a)/len(a)
    print(f'#{case + 1} {round(avg)}')

