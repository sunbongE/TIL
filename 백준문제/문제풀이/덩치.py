# 첫 줄에는 전체 사람의 수 N이 주어진다. 
# 그리고 이어지는 N개의 줄에는 각 사람의 몸무게와 키를 나타내는 
# 양의 정수 x와 y가 하나의 공백을 두고 각각 나타난다.
import sys
sys.stdin = open('덩치.txt','r')
N = int(input())

xy_li = []
for _ in range(N):
    x, y = map(int, input().split())
    xy_li.append((x,y)) #[(55, 185), (58, 183), (88, 186), (60, 175), (46, 155)]


for i in xy_li:
    cnt = 1
    for j in range(len(xy_li)):
        if i[0] < xy_li[j][0] and i[1] < xy_li[j][1]:
            cnt +=1 
    print(cnt,end=' ')

    
 