import sys
sys.stdin = open('1926.txt','r')

n = int(input())
for i in range(1, n+1):
    li = str(i)
    cnt = 0
    for num in li:
        if num in '369':
            cnt += 1
    if cnt == 0:
        print(li, end=' ')
    else:
        print('-'*cnt, end=' ')
