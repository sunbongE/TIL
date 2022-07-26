import sys

sys.stdin = open('2056.txt', 'r')

t = int(input())

for case in range(1,t+1):
    a = input() # 문자열~~ str
    y = a[:4]
    m = a[4:6]
    d = a[6:]


    if int(m) < 1 or int(m) >12 :
        print(f'#{case}',-1)
    if int(m) == 1 or int(m) == 3 or int(m) == 5 or int(m) == 7 or int(m) == 8 or int(m) == 10 or int(m) == 12:
        if int(d) >= 1 and int(d) <= 31:
            print(f'#{case}',end=" ")
            print(y,m,d,sep="/") 
    if int(m) == 9 or int(m) == 11 or int(m) == 4 or int(m) == 6:
        if int(d) >= 1 and int(d) <= 30:
            print(f'#{case}',end=" ")
            print(y,m,d,sep="/") 
    if int(m) == 2:
        if int(d) >= 1 and int(d) <= 28:
            print(f'#{case}',end=" ")
            print(y,m,d,sep="/")
        else:
            print(f'#{case}',-1)


    