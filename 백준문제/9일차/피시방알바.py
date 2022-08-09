# 값이 2 라면 출력
import sys
sys.stdin = open('피시방알바.txt','r')
dic = {}
N = int(input())

li = map(int, input().split())
for num in li:
    dic[num] = dic.get(num,0)+1
cnt = 0
for k in dic:
    if dic[k] > 1:
        cnt += dic[k] - 1
    
print(cnt)