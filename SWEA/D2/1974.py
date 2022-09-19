# 스도쿠 검증
from pprint import pprint
import sys
sys.stdin = open('1974.txt')

# 9x9
# 전체를 한 리스트에 입력받음
# 첫번째 조건은 입력 받은 리스트에 1~9가 모두 한번씩 있는가 
# 2번째 2중리스트 느낌으로 순회가야하는데 아마도 
# [[a],[b],[c],[d]] a에 첫번째 b의 첫번째를 순회할 수 있게
# 3번째는 파리채 문제 느낌으로 3중 for문으로 순회한 값을 조회#
a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for case in range(int(input())):
    ans = 1
    result = []
    for _ in range(9):
        sudoku = list(map(int, input().split()))
        
        for i in range(9):
            if a[i] not in sudoku: # 첫번째 조건 가로 줄 숫자 비교
                ans=0
            
        result.append(sudoku)
    
    # 두번째 조건
    for x in range(9):
        b = []
        for y in range(9):            
            b.append(result[y][x])
        # print(b)
        for i in range(9): # 위에 비교문 그대로 가져옴
            if a[i] not in b: 
                ans=0
    
    # 세번째
   
    for sj in range(0,9,3): # 0~5
        for sq in range(0,9,3):
            c = []
            for j in range(sj,sj+3):
                for q in range(sq,sq+3):
                    c.append(result[j][q])

            for i in range(9): # 위에 비교문 그대로 가져옴
                if a[i] not in c: 
                    ans=0

    print(f'#{case+1} {ans}')
                

         
    
        
            

    # pprint(result)