n = int(input())  
arr = [list(map(int,input())) for _ in range(n)]
v = [[0]*n for _ in range(n)]

def dfs(si,sj):
    global cnt, v
    v[si][sj] = 1
    cnt+=1
    for di,dj in ((-1,0),(1,0),(0,-1),(0,1)):
        ni,nj = si+di, sj+dj
        if 0<=ni<n and 0<=nj<n and  arr[ni][nj]==1 and v[ni][nj]==0:
            v[ni][nj]=1
            dfs(ni,nj)
ans=[]
for i in range(n):
    for j in range(n):
        if arr[i][j] == 1 and v[i][j] == 0:
            cnt=0
            dfs(i,j)
            ans.append(cnt)
ans.sort()
print(len(ans),*ans, sep='\n')
