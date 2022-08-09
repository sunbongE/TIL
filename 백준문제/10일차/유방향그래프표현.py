# 그래프 입력이 주어질 때 유방향 그래프를 
# 인접 행렬과 인접 리스트로 표현하세요.
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.  
# 둘째 줄부터 M개의 줄에 간선의 시작점 u와 끝점 v가 주어진다. 
# (1 ≤ u, v ≤ N, u ≠ v) 
# 인접 행렬을 출력하고, 인접 리스트를 출력하세요.

import sys
from pprint import pprint
sys.stdin = open('무방향.txt','r')

n,m = map(int,input().split())# 6 
graph = [[] for _ in range(n+1)] # lisy
mat = [[0]*(n+1) for _ in range(n+1)] # matrix

for _ in range(m):
    y,x = map(int,input().split())
    #y를 x에 넣기만 하면 되네
    mat[y][x] = 1
    graph[y].append(x)


pprint(mat)
pprint(graph)