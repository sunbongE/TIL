# 균형잡힌 세상
import sys
sys.stdin = open('균형잡힌세상.txt','r')


while 1:
    st = input()
    if st == '.':
        break
    situation = []
    temp = True
    
    for i in st:
        if i == '(' or i == '[':
            situation.append(i)
        elif i == ')':
            if not situation or situation[-1] == '[':
                temp = False
            elif situation[-1] == '(':
                situation.pop()
        elif i ==']':
            if not situation or situation[-1] == '(':
                temp = False
            elif situation[-1] == '[':
                situation.pop()
    if temp == True and not situation:
        print('yes')
    else:
        print('no')