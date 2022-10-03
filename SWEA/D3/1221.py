import sys
sys.stdin = open('1221.txt')
from pprint import pprint

chan = {
    "ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9
}


for _ in range(int(input())):
    li = input().split()
    case = li[0]
    N = int(li[1])
    string = input().split()
    # print( case, N)
    for i in range(N):
        for ch in chan.keys():
            if string[i] == ch:
                string[i] = chan[ch]
                # print(st)
    string.sort()

    for i in range(N):
        for k,v in chan.items():
            if string[i] == v:
                string[i] = k
    print(case)
    print(*string)


