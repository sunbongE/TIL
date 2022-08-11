import sys
sys.stdin = open('애너그램.txt','r')

for _ in range(int(input())):
    a,b = input().split()
    
    a2 = sorted(a)
    b2 = sorted(b)
    
    if a2 == b2:
        print(f'{a} & {b} are anagrams.')
    else:
        print(f'{a} & {b} are NOT anagrams.')