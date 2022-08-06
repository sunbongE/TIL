import sys
sys.stdin = open('직사각형길이찾기.txt','r')

testcase = int(input())

for case in range(1,testcase+1):
    a, b, c = map(int, input().split())
    if a == b and b == c: # a==b==c 이딴거 하면 안됨
        print(f'#{case} {a}') # 세변의 길이가 같으면 다 같아야함
    elif a == c: # 두개가 같으면 나머지 둘이 같아야함 
        print(f'#{case} {b}')
    elif a == b:
        print(f'#{case} {c}')
    elif c == b:
        print(f'#{case} {a}')
    