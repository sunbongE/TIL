import sys
sys.stdin = open('FBI.txt','r')

cnt = 0
for i in range(1,6):
    who = input()
    if len(who) <= 10 and 'FBI' in who:
        print(i,end=' ')
        

    else: cnt += 1
if cnt == 5:
    print('HE GOT AWAY!')
