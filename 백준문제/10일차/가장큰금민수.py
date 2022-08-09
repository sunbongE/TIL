import sys
sys.stdin = open('가장큰금민수.txt','r')
# n= int(input())
# max1 = 0
# num = 0
# for i in range(n+1):
#     four = str(i).count('4')
#     seven = str(i).count('7')
#     val = int(four) + int(seven)
#     if val >= max1:
#         max1 = val
#         num = i
# print(num)

n= int(input())
while 1:
    temp = True
    for i in str(n):
        if i != '4' and i != '7':
            temp = False
            n -= 1
    if temp:
        print(n)
        break
