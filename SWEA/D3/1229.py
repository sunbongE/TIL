import sys
sys.stdin = open('1229.txt')

for _ in range(10):
    N = int(input())
    origin = list(map(int,input().split()))

    com_cnt = int(input())
    com_li = input().split() # 리스트로 입력받고
    
    for i in range(len(com_li)):
        # 삽입
        if com_li[i] == 'I':
            loc=int(com_li[i+1])
            cnt =int(com_li[i+2])
            for n in range(cnt,0,-1):
                origin.insert(loc,com_li[i+2+n]) 
        # 삭제
        if com_li[i] == 'D':                    #D를 만나면
            loc_d = int(com_li[i+1])            # 삭제할 위치
            cnt_d = int(com_li[i+2])            # 지울 개수
            for m in range(cnt_d):
                del origin[loc_d]
    print(f'#{_+1}',end=' ')
    print(*origin[:10])