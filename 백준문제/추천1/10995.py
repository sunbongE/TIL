# 마지막 별찍?
n = int(input())

for i in range(1,n+1):
    if i % 2 == 0:
        print(" ",end ='')
    print("* "*n)


# 다른 풀이
n = int(input())

if n == 1:
    print("*")
else:
    for i in range(n):
        if i % 2 == 0:
            print("* "*n)
        else:
            print(" *"*n)
