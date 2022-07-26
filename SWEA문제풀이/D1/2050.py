word = input() #abc

for i in word:
    # print(i,type(i))# 문자형
    r = int(ord(i))-64
    print(r, end = ' ')