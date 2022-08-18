# AAAAAAAAAA
# BBBBBBBCCC
# CC
import sys
sys.stdin = open('1946.txt','r')

T = int(input())
for tc in range(1, 1+T):
    n = int(input())
    document = ''
    for _ in range(n):
        word, number = input().split()
        document += word*int(number)

    print('#{}'.format(tc))

    for i in range(0, len(document), 10): # i = 0 10 20
        print(document[i:i+10])
        # print(i)
    # print(len(document))