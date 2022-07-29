# # 오타맨 고창영
# 고창영은 맨날 오타를 낸다. 창영이가 오타를 낸 문장과 오타를 낸 위치가 주어졌을 때, 
# 오타를 지운 문자열을 출력하는 프로그램을 작성하시오.
# 창영이는 오타를 반드시 1개만 낸다.
#1 케이스 입력, 오타 위치와 문자열 입력


# 1 PROGRAMMING
# 7 CONTEST
# 3 BALLOON
case = int(input())# 4

for a in range(1,1+case):# 4 MISSPELL -> MISPELL
    #오타까지 출력하고 다음 문자를 붙여서 출력
    #일단 입력을 받아야함
     n, w = map(str, input().split())
     n=int(n)
     print(w[:n-1]+w[n:])