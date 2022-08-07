import sys
# sys.stdin = open('공.txt','r')
 
N = int(input())

cups = [1,2,3]
for _ in range(N):
    x, y = map(int, input().split())
    
    xi = cups.index(x)
    yi = cups.index(y)
    # print(xi)
    cups[xi], cups[yi] = cups[yi], cups[xi]
    
print(cups[0])


