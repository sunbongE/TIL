# 맨 왼쪽 두 칸과 맨 오른쪽 두 칸에는 건물이 지어지지 않는다. 
# 음.. 아무래도 높이 최대 255를 활용해야할듯 컨프리헨션으로
# arr 만들고 w는 가로 #
import sys
from pprint import pprint
sys.stdin = open('1206.txt')

for case in range(2):
    w = int(input())
    li=list(map(int, input().split()))
    arr = [[0]*w for _ in range(max(li))] # 이거 이용해서
    # for y in range(255,255-max(li),-1):

    for x in range(w):
        for y in range(max(li)-1,max(li)-max(li),-1):
            if y == max(li)-1-li[x]:
                break
            # print(y,(max(li)-li[x]))
            arr[y][x] = 1
    # 건물 구현했고 이제 비교하면됨 가로 순회
    ans = 0
    for y in range(max(li)-1,max(li)-max(li),-1):
        cnt = 0
        for x in range(2,w-2):
            if arr[y][x-1] + arr[y][x-2] + arr[y][x+1] + arr[y][x+2] == 0:
                cnt+=1
        ans += cnt
        #     print(arr[y][x-1],arr[y][x],arr[y][x+1])
        # print()
    print(cnt)
# pprint(arr)

