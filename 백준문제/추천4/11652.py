#카드문제
import sys
sys.stdin = open('11652.txt', 'r')

dic = {}
N = int(sys.stdin.readline())
for _ in range(N):
    num = int(sys.stdin.readline())
    dic[num] = dic.get(num,0) + 1
dic = sorted(dic.items())
max_ = 0
result = 0
for i, c in dic:
    if c > max_:
        max_ = c
        result = i
print(result)
