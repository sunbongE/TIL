import sys
sys.stdin = open('암기왕.txt','r')


for _ in range(int(input())):
    n1 = int(sys.stdin.readline())
    li1 = list(map(int,sys.stdin.readline().split()))
    n2 = int(sys.stdin.readline())
    li2 = list(map(int,sys.stdin.readline().split()))
    for i in li2:
        if i in li1:
            print(1)      
        else: print(0)
# note1 = {n1:0 for n1 in li1}
# print(note1)