for _ in range(int(input())):

    m,n=map(int,input().split())    

    li = []
    ans=0
    for _ in range(m):
        li.append(input().split())
    
    for i in range(n):
        cnt=0
        for j in range(m-1,-1,-1):
            if li[j][i] == '1':
                ans += cnt
            else:
                cnt += 1
    print(ans)