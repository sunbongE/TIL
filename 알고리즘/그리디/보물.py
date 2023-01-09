N = int(input())    

A = list(map(int,input().split()))
B = list(map(int,input().split()))
A.sort(reverse=True)
B.sort()
ans = 0
for i in range(N):
    ans += A[i]*B[i]
print(ans)