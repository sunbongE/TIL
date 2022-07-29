#b d p q 를 거울로 바꾼모습 보이기
import sys
sys.stdin = open('문자열의거울상.txt','r')
testcase = int(input())

for case in range(1,testcase + 1):
    #순회하며 무엇을 받았는지 알아보고 
    #해당 글자의 거울모양을 if로 해야겠다.
    #입력
    st = input()
    result = ''
    for w in st: # W는 b  d  p  q 이런식으로 하나하나 나옴
        if w == 'b':
            result += 'd'
            
        elif w == 'd':
            result += 'b'

        elif w == 'p':
            result += 'q'

        elif w == 'q':
            result += 'p'
    print(f'#{case} {result[::-1]}') #뒤집어서 출력해야 거울느낌나옴
        