# # 출퇴근 인원 현황 구하기
 
# import sys
# sys.stdin = open('7785.txt','r')
# # N = int(input())
# dic_ = {}
# for p in range(N):
    
#     employee, st = input().split()
#     dic_[employee] = st
#     if dic_[employee] == 'leave': 
#         del dic_[employee]
# dic_=sorted(dic_, reverse= True)
# print('\n'.join(dic_))

#-----------------------------------------------------------------

import sys
sys.stdin = open('7785.txt','r')
N = int(input())
company = {}
 
for p in range(N):
    
    person, attend = input().split()
    company[person] = attend
enter_list = []
for k,v in company.items():
    if v == 'enter':
        enter_list.append(k)
enter_list.sort(reverse=True)
print('\n'.join(enter_list))


#-----------------------------------------------------------------
import sys
sys.stdin = open('7785.txt','r')
company = dict()

n = int(sys.stdin.readline().strip())

for _ in range(n):
    person, attend = sys.stdin.readline().split()
    company[person] = attend
# print(person, attend)
enter_list = []

for k, val in company.items():
    if val == 'enter':
        enter_list.append(k)

enter_list.sort(reverse= True)

print('\n'.join(enter_list))
# '\n' 개행을 enter_list 사이에 조인한다는 의미

