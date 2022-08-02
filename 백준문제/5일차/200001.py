#고무오리 디버깅
import sys 
# sys.stdin = open('고무오리.txt','r') 입력이 잘 안된다

cnt = 0 

while 1:
    w = input()
    if w == '문제':
        cnt += 1
    elif w == '고무오리':
        if cnt == 0 :
            cnt += 2
        else: cnt -= 1
    elif w == '고무오리 디버깅 끝':
        break
if cnt == 0: print('고무오리야 사랑해')
else: print('힝구')