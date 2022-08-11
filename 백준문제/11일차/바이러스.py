import sys
from pprint import pprint
sys.stdin = open('바이러스.txt','r')


com = int(input()) # 7
graph = [[] for _ in range(com+1)]
visited = [False] * (com+1)
# [False, False, False, False, False, False, False, False]
# 0~7
# print(visited)
total = 0

for _ in range(int(input())):# 6
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
#인접 리스트 (무방향)

start = 1 
stack = [start]
visited[start] = True
# 0번 변경
while stack:
    cur = stack.pop()

    for adj in graph[cur]: # [2,5]
        if not visited[adj]:#visited[2] 여기가 False면
            visited[adj] = True
            stack.append(adj)
print(sum(visited)-1)
print(visited)




# print(li)# [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]


# while 1:
    

# '''
# [[],[2,5],[1,3,5],[2,],[7],[1,2,6],[5],[4]]

# 1- 2,5
# 2- 1,3,5
# 5- 6
# '''