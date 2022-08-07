import sys
sys.stdin = open('단어뒤집기.txt','r')

t = int(input())

for _ in range(t):  
    li=(input().split())
    for i in range(len(li)):
        print(li[i][::-1],end=' ')
    print()

# I ma yppah yadot
# eW tnaw ot niw eht tsrif ezirp
# I ma yppah yadot 
# eW tnaw ot niw eht tsrif ezirp 
