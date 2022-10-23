# 팩토리얼

def fac(n):
    if n== 1:              # base condition
        return 1 
    return n * fac(n-1)     
# 5 * fac(4)
# 4 * fac(3)
# 3 * fac(2)
# 2 * fac(1)
print(fac(5)) 