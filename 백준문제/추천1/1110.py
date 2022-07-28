# 더하기 사이클
#  1. 만약 수가 10보다 작으면 뒤에 0 붙이고, 각자리 수를 더함
# 2. 원래 수의 1의 자리 수와 더한 수를 .. 

n1 = (input())
n = n1
sycle = 0
while 1:

    if len(n) == 1: # 한 자리 숫자인 경우
        n = "0" + n
        new_n = n[1] + str(int(n[0])+int(n[1]))[-1] # str

        #1번 각 자리수를 더한다.
    new_n = n[1] + str(int(n[0])+int(n[1]))[-1]
    sycle += 1
    n = new_n
    if int(n1) == int(new_n): # 0 == 00 이래서 int사용
        
        break



print(sycle)