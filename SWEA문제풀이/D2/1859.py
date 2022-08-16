import sys
# sys.stdin = open('1859.txt')
sys.stdin = open('t.txt')


for t in range(int(input())):
    buy_li = []
    n = int(input())
    li = list(map(int,input().split()))
    for i in range(1,len(li)):
        if li[i-1] <= li[i]:
            buy_li.append(li[i-1])
        else: print(li[i-1])

    print(buy_li)