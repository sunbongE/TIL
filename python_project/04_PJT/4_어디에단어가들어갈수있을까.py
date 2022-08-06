import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")
# sys.stdin = open("t.txt")
t = int(input()) # 10
for case in range(1,1+t): 
    n, k = map(int, input().split())# 5 3 
    mat = [list(map(int, input().split())) for _ in range(n)]
# pprint(mat)
    result_x = 0
    for a in mat: # 하나씩 리스트 가져ㅛ옴
        cnt_x = 0
        
        
        for i in range(len(a)): # 한줄에 3이 두개면 0이되어야함.....
            # print(a[i],end=' ')
            
            if a[i] == 1: # 리스트 안에 요소가 1이면
                cnt_x += 1 # 늘리고
            else: # 1아니면서      _y       
                if cnt_x == k : # cnt_y 3이면 
                    result_x += 1 # 값으로_y 1 증가 
                    cnt_x = 0 # 증가하고 cnt_y 0
                else: cnt_x = 0
        # print(result_x)
        else:
            if cnt_x == k:
                result_x += 1
        # if result == 2:
        #     result = 0 
        # else:
        #     result_x += result

        # print()
    # print(result_x) # 2
    
    result_y = 0
    for i in range(n):
         
        cnt_y =0 
        for j in range(n):
            
            # print(mat[j][i],end=' ')
            if mat[j][i] == 1:
                cnt_y += 1 
            else:
                if cnt_y == k:
                    result_y += 1
                    cnt_y = 0
                else: cnt_y = 0
        else:
            if cnt_y == k:
                result_y += 1
        # if result == 2:
        #     result = 0 
        # else:
        #     result_y += result
        # print()
        # print(cnt_y,result_y)
    print(f'#{case} {result_y+result_x}')
    # print(result_x,result_y) 모름..