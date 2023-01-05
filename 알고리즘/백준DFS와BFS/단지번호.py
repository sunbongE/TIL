

N= int(input()) 
arr = [list(map(int,input())) for _ in range(N)]

total = 0
cnt_list= []

for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            dfs(i,j)

