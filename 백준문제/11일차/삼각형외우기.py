import sys
sys.stdin = open('삼각형.txt','r')
li=[]
for _ in range(3):
    li.append(int(input()))

if li[0] == 60 and li[1] == 60 and li[2] == 60:
    print('Equilateral')
elif sum(li) == 180 and (li[0]==li[1] or li[1]==li[2] or li[2]==li[0]):
    print('Isosceles')
elif sum(li) == 180 and (li[0]!=li[1] and li[1]!=li[2]):
    print('Scalene')
elif sum(li) != 180:
    print('Error')