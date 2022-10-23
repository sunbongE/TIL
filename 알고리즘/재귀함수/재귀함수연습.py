def func_b(n):
    if n >= 4:
        return
    print(type(n))
    print(n,end=' ')
    func_b(n+1)     
    print(n,end=' ')

func_b(0)  # 0 1 2 3 3 2 1 0 

N=4
def prac(n):
    if n == 1:
        print(n,end=' ')
        return 
    print(n,end=' ')
    prac(n-1)
    print(n,end=' ')
prac(N) # 4 3 2 1 2 3 4 

def prac(n):
    if n == 0:
        return
    print(5-n,end=' ')
    prac(n-1)
    print(n,end=' ')
prac(N)


#-------------------------------
# li=[]
# def prac(n):
#     if n > 4:
#         return
#     li.append(n)
#     print(*li)
#     prac(n+1)    
# prac(1)
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# def prac(n):
#     if n > 4:
#         return
#     for i in range(1,n+1):
#         print(i,end=' ')
#     print()
#     prac(n+1)    
# prac(1)
# #-------------------------------
# a = 4
# subset = [0] * a
# for i in range(1<<a):
#     for j in range(a):
#         subset[j] = 1 if i & (1<<j) else 0 
#     print(subset)