
import sys
input = sys.stdin.readline
n=int(input())
days=[0,31,28,31,30,31,30,31,31,30,31,30,31]
# # 3/1: 60 ~ 12/1: 335
for i in range(1,12):
    days[i] = days[i-1] + days[i]
flowers = [0]*366


for i in range(n):
    f = list(map(int, input().split()))
    # 월을 일수로 변환하는 작업
    flowers[days[f[0]-1]+f[1]] = max(days[f[2]-1]+f[3], flowers[days[f[0]-1]+f[1]])

end = 60
maxi = 0
cnt = 0
for i in range(1,366):
    maxi = max(maxi, flowers[i])
    if i == end:
        if maxi > end:
            cnt += 1
            if maxi >= 335:
                break
            end = maxi
            continue
        else:
            break
        
if maxi >= 335:
    print(cnt)
else:
    print(0)