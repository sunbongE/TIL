def f(n): # 피보나치랑 같음
    if d[n]:
        return d[n]
    else:
        d[n] = f(n-1) + f(n-2)
        return d[n]
    
    
num = int(input())   
if num > 2:
    d = [0]*(1+num)
    d[1] = 1
    d[2] = 1
    print(f(num))
else:
    print(1)
