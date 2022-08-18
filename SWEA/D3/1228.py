#암호문
import sys
sys.stdin = open('암호문.txt','r')

for tc in range(1,11):
    a = int(input())
    b = list(map(int, input().split()))
    c = int(input())
    d = list(input().split()) # 조건 암호열
    for i in range(len(d)):#  명령 암호의 개수 만큼 
        if d[i] == 'I': #I를 만나면 
            idx = int(d[i+1]) # ind변수에 I다음 자리 저장 ( 자리수 ) |위치 1
            nums = int(d[i+2]) # 들어갈 숫자의 개수 | 5
            # print(idx,nums)

            for j in range(nums): # 들어갈 숫자의 개수만큼 반복 
                # print(j)
                b.insert(idx+j,int(d[i+2+(j+1)])) #(1+0,)
                # 원래 암호에 삽입 -> inser(위치, 값) d[3] [0+2+(0+1)]
                #idx가 1이고 j가 0부터 증가하니까
                # 시작점을 맞춰준거라 생각하면된다.
                # d는 암호들 처음 7개 중 몇번째에 접근하는지 
                # 0+2+(0+1) i가 0부터 7까지

                # print(d[])
        # else: # 없어도댐
        #     continue
    # print('#{} {}'.format( tc,' '.join(map(str,b[:10]))))
print(len(b))