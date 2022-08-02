# 균형잡힌 세상
import sys
sys.stdin = open('균형잡힌세상.txt','r')


while 1:
    st = input()
    if st == '.':
        break
    small_ = []
    big_ = []
    
    for w in st:
        
        if w == '(':
            small_.append(w)
        elif w == ')':
            if small_ : 
                small_.pop()
            else: print('no'); break
        if w == '[':
            big_.append(w)
        elif w == ']':
            if big_: big_.pop()
            else: print('no'); break
    else:
        if len(big_) == 0 and len(small_) == 0:
            print('yes')
        
        else:
            print('no')

#Help( I[m being held prisoner in a fortune cookie factory)].