import sys
sys.stdin = open('트럭주차.txt','r')

# a,b,c = map(int, input().split())

# t1 = list(map(int, sys.stdin.readline().split()))
# t2 = list(map(int, sys.stdin.readline().split()))
# t3 = list(map(int, sys.stdin.readline().split()))
# # [1, 6] [3, 5] [2, 8]
# last_time = max(t1[1],t2[1],t3[1]) # 8 

# fee = 0
# for time in range(1,last_time+1):
#     t_cnt = 0
#     if t1[0] < time <= t1[1]:
#         t_cnt += 1 

#     if t2[0] < time <= t2[1]:
#         t_cnt += 1 
        
#     if t3[0] < time <= t3[1]:
#         t_cnt += 1 
    

#     if t_cnt == 1:
#         fee += a*t_cnt
#     elif t_cnt == 2:
#         fee += b*t_cnt
#     elif t_cnt == 3:
#         fee += c*t_cnt
#     # print(t_cnt,time,fee)
# print(fee)
A, B, C = map(int, input().split())

arr = [0]*100
answer = 0
for _ in range(3):
    start, end = map(int, input().split())
    for i in range(start, end):
        arr[i] += 1

for j in arr:
    answer += {0: 0, 1: A, 2: B*2, 3: C*3}[j]
    print(j)
print(answer)