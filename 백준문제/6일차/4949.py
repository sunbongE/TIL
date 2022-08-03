# 균형잡힌 세상
import sys
sys.stdin = open('균형잡힌세상.txt','r')


while 1:
    st = input()
    if st == '.':
        break
    small_ = []
    big_ = []
    # ([ (([( [ ] ) ( ) (( ))] )) ])
    # '(',
    # 
    for w in st:
        cnt = 0
        if w == '(':
            small_.append(w)
        elif w == ')': # ) 면서
            
            if small_ : # 소괄호가 비어있지않고
            
                small_.pop()
                
                    
            else: print('no'); break
        if w == '[':
            big_.append(w)
            cnt += 1
        elif w == ']':
            if big_: big_.pop(); cnt -= 1
                
            else: print('no'); break
    else:
        if len(big_) == 0 and len(small_) == 0:
            print('yes')
        
        else:
            print('no')

#Help( I[m being held prisoner in a fortune cookie factory)].