import sys
sys.stdin = open("1215.txt")
from pprint import pprint
for case in range(10):
    leng = int(input())
    cnt = 0

    pan = []
    for _ in range(8):
        w = input()
        pan.append(w)
        for n in range(8-leng+1): # 가로비교
            pal = w[n:n+leng]
            if pal == pal[::-1]:
                cnt+=1
        #     print(pal,pal[::-1])
        # print(cnt)
    
    # 세로 비교
    # print(pan)
    for y in range(8):
        new_=''
        for x in range(8):
            pal = pan[x][y]
            new_ += pal
            
            
        # print(new_)    

        for n in range(8-leng+1): # 가로비교
            pal = new_[n:n+leng]
            # print(pal)
            if pal == pal[::-1]:
                cnt+=1

    print(f'#{case+1} {cnt}')


