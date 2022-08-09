import sys
from pprint import pprint
sys.stdin = open('무방향.txt','r')

# 그래프 입력이 주어질 때 무방향 그래프를 인접 행렬과
#  인접 리스트로 표현하세요.
# 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다.
#   둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다.
#  (1 ≤ u, v ≤ N, u ≠ v) 
# 인접 행렬을 출력하고, 인접 리스트를 출력하세요.

n,m = map(int,input().split())# 6 5

graph = [[] for _ in range(n+1)]# 리스트를 만들었음


mat = [[0]*(n+1) for _ in range(n+1)]
# pprint(mat) # 6x6 행렬을 만들었음
for i in range(m):
    y,x = map(int, input().split())
    mat[y][x] = 1
    mat[x][y] = 1
    graph[y].append(x) # y번째 리스트에 x를 추가시킴
    graph[x].append(y) # 서로 이어져 있다.



pprint(mat) # 행령 표현
print(graph)

