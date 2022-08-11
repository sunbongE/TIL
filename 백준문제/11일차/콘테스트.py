
import sys
sys.stdin = open('콘테스트.txt','r')
total = []
for _ in range(20):
    total.append(int(input()))
W = total[:10]
W.sort(reverse=True)
K = total[10:]
K.sort(reverse=True)
print(sum(W[:3]),sum(K[:3]))