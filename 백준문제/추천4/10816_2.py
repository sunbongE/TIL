import sys 
sys.stdin = open('10816.txt','r')

N = int(input())
N_nums = list(map(int, input().split()))
M = int(input())
M_nums = list(map(int, input().split()))
dic_N = dict()
#N_nums를 딕셔너리의 형태로 정리한다.
for num in N_nums:
    dic_N[num] = dic_N.get(num, 0) +1

# print(dic_N)
for num in M_nums:
    result = dic_N.get(num)
    if result == None:
        print(0,end=' ')
    else:
        print(result,end=' ')
