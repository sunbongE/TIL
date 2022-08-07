# 두수 합 구하기

# 5->6 최대 6->5 최소
import sys
sys.stdin = open('5와6차이.txt','r')

a, b = input().split()  

for w in a:
    if w == '6':
        a = a.replace('6','5')
for w in b:
    if w == '6':
        b = b.replace('6','5')
min_ = int(a)+int(b)

for w in a:
    if w == '5':
        a = a.replace('5','6')
for w in b:
    if w == '5':
        b = b.replace('5','6')
max_ = int(a)+int(b)
print(min_,max_)
