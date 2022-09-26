import sys
sys.stdin = open('1208.txt')


for case in range(10):
    dump = int(input())
    li = list(map(int, input().split()))


    for _ in range(dump):
        max_num = li.pop(li.index(max(li)))
        li.append(max_num-1)
        min_num = li.pop(li.index(min(li)))
        li.append(min_num+1)
    ans=max(li)-min(li)
    print(f'#{case+1} {ans}')

