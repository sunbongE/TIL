import sys
sys.stdin = open('1209.txt')
from pprint import pprint
for _ in range(10):
    case = input()
    arr = []
    for n in range(100):
        li = list(map(int, input().split()))
        arr.append(li)
    total=[]
    hang = []
    yul = []
    cross1=[]
    cross2=[]
    # 행
    for y in range(100):
        hap = 0
        for x in range(100):
            
            hap += arr[y][x]
        hang.append(hap)
    total.append(max(hang))
    # 열
    for y in range(100):
        hap = 0
        for x in range(100):
            
            hap += arr[x][y]
        yul.append(hap)
    total.append(max(yul))

    # 대각선 왼쪽에서 오른쪽아래
    for y in range(100):
        hap = 0
        for x in range(y,y+1):
            
            hap += arr[y][x]
        cross1.append(hap)
    total.append(sum(cross1))

    # 반대 대각선 
    for y in range(100):
        hap = 0
        for x in range(99-y,99-y+1):
            
            hap += arr[y][x]
        cross2.append(hap)
    
    total.append(sum(cross2))
    ans=max(total)
    print(f'#{case} {ans}')