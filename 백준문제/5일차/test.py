# 3 x 3 행렬
from pprint import pprint
n = 8
m = 7
hang = []
# for i in range(n):
#     hang.append([i]*m)
# pprint(hang)

# print(hang.append([list(map(int,input().split())) for _ in range(n)]))
'''
n x m 크기의 입력을 받아보자
3 4
1 2 3 4 
5 6 7 8 
9 0 1 2

'''
result = [(list(map(int, input().split()))) for _ in range(3)]
pprint(result)