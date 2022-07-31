#듣보잡 구하기
#접근법
#한번에 입력을 받으면서 딕셔너리로 만듬, 두번 나온 사람은 듣보잡
#value가 1보다 크면 듣보잡이니까 새로운 리스트에 담아 출력

import sys
sys.stdin = open('1764.txt','r')
N,M = map(int, sys.stdin.readline().split())
# print(N,M)
dic_name = {}
for _ in range(N+M):
    name = sys.stdin.readline().strip()
    dic_name[name] = dic_name.get(name,0)+1
result = sorted(dic_name.items())

li=[]
for n, c in result:
    if c > 1:
        li.append(n)
print(len(li),'\n'.join(li),sep='\n')