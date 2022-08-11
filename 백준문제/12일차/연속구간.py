import sys
sys.stdin = open('연속구간.txt','r')

# 연속 수가 없으면 1
# 있으면 가장 긴 구간

for _ in range(3):
    n = input()
    ans = 1
    cnt = 1
    for i in range(1,len(n)):
        if n[i] == n[i-1]:
            cnt += 1
            if ans < cnt:
                ans = cnt
        else: cnt = 1
    print(ans)