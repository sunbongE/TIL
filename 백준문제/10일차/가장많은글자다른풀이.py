import sys
sys.stdin = open('가장많은글자.txt','r')

# 길이 결과값을 저장할 리스트
li = [0]*26 #a-z

# sys.stdin.read()를 통해 입력을 eof 날 때 까지 받을 수 있다.
# 또한 try, except를 이용하여, 입력을 eof 날 때 까지 받을 수 있다.
s = sys.stdin.read().replace('\n','').replace(' ','')

# li 리스트의 0번 인덱스(a)부터 해당 문자가 존재한다면 1씩 추가해준다.
for i in s:
    li[ord(i)-97] += 1
#ord('a') = 97 

for j in range(26):
    # 만약 리스트의 인덱스가 최댓값과 같다면(최댓값이 여러개라면)
    if li[j] == max(li):
        # 문자를 알파벳 순서에 따라 출력한다.
        print(chr(97+j), end ='')
