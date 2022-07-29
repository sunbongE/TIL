import sys
sys.stdin = open('암호문.txt','r')

for case in range(1,11):
    N = int(input())
    se = list(map(str, input().split()))
    cm_cnt = int(input())
    cm = list(map(str, input().split('I ')))
    cm.remove(cm[0])
    
   