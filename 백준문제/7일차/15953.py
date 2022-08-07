import sys
sys.stdin = open('상금헌터.txt','r')
dic1 = {
    '0':0,
    '1': 500,
    '2': 300,
    '3': 200,
    '4': 50,
    '5': 30,
    '6': 10    
}
dic2 = {
    '0': 0,
    '1': 512,
    '2': 256,
    '4': 128,
    '8': 64,
    '16': 32    
}
t = int(input())
for _ in range(t):
    a, b = map(int,input().split()) # 8 4
    rank = 0
    cnt = 0
    for x in dic1:
        cnt += int(x)
        if a <= cnt:
            rank = x
            break
        elif a > 21 or a == 0:
            rank = '0'
    result1 = dic1[rank]*10000 # 1 번째 상금
    rank2 = 0
    cnt2 = 0
    for y in dic2:
        cnt2 += int(y)
        if b <= cnt2:
            rank2 = y
            break
        elif b > 31 or b == 0:
            rank2 = '0'
    result2 = dic2[rank2]*10000 # 2 번째 상금
    print(result1+result2)