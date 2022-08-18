# 1 3 5 7 8 10 12 = 31
# 2월 = 28
# 4 6 9 11 = 30#
import sys
sys.stdin = open('t.txt','r')
dic = {
    1:31,
    2:28,
    3:31,
    4:30,
    5:31,
    6:30,
    7:31,
    8:31,
    9:30,
    10:31,
    11:30,
    12:31
}
for t in range(int(input())):
    m1,d1,m2,d2 = list(map(int,input().split()))
    ans = 0
    for a in range(m1,m2):
        if m1 == a:
            ans += dic[m1] - d1 + 1
           
        else:
            ans += dic[a]
    ans += d2 
    print(f'#{t+1} {ans}')