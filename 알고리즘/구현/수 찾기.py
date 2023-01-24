# 시간초과로 딕셔너리 사용
m=int(input())
A = input().split()
a_dic = dict()
for a in A:
    a_dic[a] = 1

n=int(input())
x_list = list(map(int,input().split())) 

for x in x_list:
    try:
        print(a_dic[str(x)])
    except:
        print(0)
# 시간 초과로 중복제거
# n = int(input())
# n_list = set(map(int, input().split()))
# m = int(input())
# m_list = list(map(int, input().split()))

# for i in m_list:
#     if i in n_list:
#         print(1)
#     else:
#         print(0)