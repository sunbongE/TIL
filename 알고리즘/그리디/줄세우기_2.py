import sys
input = sys.stdin.readline
n = int(input())    

child = [0] + list(map(int,input().split()))
position = [0] * (n+1)

for i in range(1,n+1):
    position[child[i]] = i
# print(position)
cnt = 1
maxi=0
for x in range(1,n): 
    if position[x] < position[x+1]:
        cnt += 1
        maxi = max(cnt,maxi)
    else: cnt=1
print(n-maxi)

