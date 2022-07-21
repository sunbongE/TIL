import sys
sys.stdin = open('1288.txt','r')



t = int(input())

for i in range(1,t+1):
    n = int(input())
    c = 0
    result = []
    new_result = {}
    while len(new_result) != 10:
        
        n1 = int(n)
        c += 1
        n1 *= c
        n1= str(n1)
        
        
        for j in n1:            
            result.append(j)
            
            new_result = set(result)
        # print(new_result,n1)

    print(f'#{i}',n1)

