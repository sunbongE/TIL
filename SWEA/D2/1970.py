import sys
sys.stdin = open('1970.txt')

changes=[50000, 10000, 5000, 1000, 500, 100, 50, 10]
result=[0, 0, 0, 0, 0, 0, 0, 0,]
for case in range(int(input())):
    pay = int(input())

    for i in range(len(changes)):
        cnt = pay // changes[i]
        pay = pay % changes[i]
        result[i] = cnt
    print(f'#{case+1}')
    print(*result)