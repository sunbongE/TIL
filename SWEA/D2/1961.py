from posixpath import split
import sys
sys.stdin = open("1961.txt")

for case in range(int(input())):
    N = int(input())
    arr=[]
    for i in range(N):
        a = input().split()
        arr.append(a)
        
   
    new_arr = []
    result = []
    for _ in range(3):
        for y in range(N):
            new=''
            li=[]   

            for x in range(N):
                # print(arr[N-1-x][y])
                n_arr = arr[N-1-x][y]
                li.append(n_arr)

                new += arr[N-1-x][y]
            
            new_arr.append(li)
            result.append(new)
        arr = new_arr
        new_arr=[]
    print(f'#{case+1}')
    for x in range(N):
        print(*result[x::N])


