#암호문
import sys
sys.stdin = open('암호문.txt','r')

for _ in range(10):
    N = int(input())
    origin = list(map(int,input().split()))

    com_cnt = int(input())
    com_li = input().split()
    
    for i in range(len(com_li)):
        if com_li[i] == 'I':
            loc=int(com_li[i+1])
            cnt =int(com_li[i+2])                   # I위치에서 2칸 뒤는 반복 횟수 즉,y의 위치
            for n in range(cnt,0,-1):               # 뒤에서부터 삽입
                origin.insert(loc,com_li[i+2+n])    #
                # print(loc,com_li[i+2+n])
    print(f'#{_+1}',end=' ')
    print(*origin[:10])



    # print(N)
    # print(origin)
    # print(com_cnt)
    # print(com_li)
