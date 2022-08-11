import sys
sys.stdin = open('행복한지슬픈지.txt','r')
feel = input()
sad = feel.count(':-(')
happy = feel.count(':-)')
if sad > happy:
    print('sad')
elif sad < happy:
    print('happy')
elif sad != 0 and happy != 0 and sad == happy:
    print('unsure')
else:
    print('none')