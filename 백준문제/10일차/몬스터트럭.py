import sys
from pprint import pprint
sys.stdin = open('몬스터트럭.txt','r')

R,C = map(int,input().split())# 4 4

mat = [list(map(str,input())) for _ in range(R)]
# pprint(mat)
p = 0
X1 = 0
X2 = 0
X3 = 0 
X4 = 0
for i in range(R-1):
    for j in range(C-1):
        
        li=[]
        re = []
        for si in range(i,i+2):
            for sj in range(j,j+2):
                car = mat[si][sj]
                li.append(car)
        if '#' not in li:
            cnt_x = li.count('X')
            if cnt_x == 1:
                X1 += 1# 부실 차 계수
            elif cnt_x == 2:
                X2 += 1
            elif cnt_x == 3:
                X3 += 1
            elif cnt_x == 4:
                X4 += 1
            else:
                p +=1
print(p)
print(X1)
print(X2)
print(X3)
print(X4)



        # print(li)
        # print('---')
