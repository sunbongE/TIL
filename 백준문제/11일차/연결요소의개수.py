import sys
sys.stdin = open('연결요소의개수.txt','r')
#인접리스트 만듬

n,m = map(int,sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]
connect = [False]*(n+1)

for _ in range(m):
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
# print(graph) 

# [[], [2, 5], [1, 5, 4, 3], [4, 2], [3, 6, 5, 2], [2, 1, 4], [4]]
# [False, False, False, False, False, False, False]
# [False, True, True, True, True, True, True]
# print(connect)
start = 1
stack = [start]                   # 시작은 1부터 했음 
connect[start] = True
cnt = 1
while sum(connect) != n:                          # DFS 
    cur = stack.pop()             
    # print(cur)
    if not graph[cur]:              # graph 가 비어있고 
        if not connect[cur]:        # 연결도 안되어있다면 cnt + 1 그리고 방문기록
            cnt += 1
            connect[cur] = True
        # print(cur,at)
    
    for at in graph[cur]:       # DFS구현
        if not connect[at]:
            connect[at] = True
            stack.append(at)
            
        if not stack and sum(connect) != n: # 스택이 비어있는데 0번째를 제외한 나머지가 True가 아니면
            cnt += 1                        # cnt + 1
            for i in range(1,len(connect)): # 1~n 중에 False라면 그 인덱스 가져와 스택으로 넣음
                if connect[i] == False:
                    stack.append(i)
                    # print(i)
    
    # if sum(connect) == n: stack.clear(); break # 1~n 전부 True 일 때 멈춤
        

print(stack, connect)
print(graph)
print(cnt)



