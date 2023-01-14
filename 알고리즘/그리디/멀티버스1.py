import sys
input = sys.stdin.readline

m, n = map(int, input().split())
d = {}

for _ in range(m):
    li = list(map(int, input().split()))
    k = sorted(list(set(li)))
    i = {k[i]: i for i in range(len(k))}
    # print(i)
    # print('이게li',li)
    c = str([i[l] for l in li])
    # print(c)
    d[c] = d.get(c, 0) + 1
# print(d)
print(sum(map(lambda x: x * (x - 1) // 2, d.values())))

# import sys
# input = sys.stdin.readline
# from collections import defaultdict

# m, n = map(int, input().split())
# universe = defaultdict(int)
# # print(universe)

# for _ in range(m):
#     # 행성 입력 받기
#     planets = list(map(int, input().split()))
    
#     # 행성 정렬 ( 구성 같은 행성 한개만 세기 )
#     sortedPlanets = sorted(list(set(planets)))
    
#     # 행성 순위 지정
#     rank = {sortedPlanets[i] : i for i in range(len(sortedPlanets))}
    
#     # 입력 받은 행성에 맞게 순위 저장
#     vector = tuple([rank[i] for i in planets])
    
#     # 해당 순위 벡터에 대한 개수 추가
#     universe[vector] += 1
    
# sum = 0

# for i in universe.values():
#     # n개 중 2개의 우주를 엮어야 하기 때문에 n C 2 를 해줘야 함 (중복 제외)
#     sum += (i * (i - 1)) // 2 # nC2
    
# print(sum)