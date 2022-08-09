import sys
sys.stdin = open('R2.txt','r')

# 평균 S 
R1 , S = map(int, input().split())
R2 = S*2 - R1
print(R2)