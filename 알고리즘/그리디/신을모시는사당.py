# 신을 모시는 사당에는 신을 조각한 돌상 N개가 일렬로 놓여 있다. 각 돌상은 왼쪽 또는 오른쪽을 바라보고 서있다. 창영이는 연속한 몇 개의 돌상에 금칠을 하여 궁극의 깨달음을 얻고자 한다.

# 궁극의 깨달음을 얻기 위해서는 가능한 한 많은 금색 돌상들이 같은 방향을 바라보아야 한다. 방향이 다른 돌상은 깨달음에 치명적이다. 깨달음의 양은 아래와 같이 정의된다.

# | (왼쪽을 바라보는 금색 돌상의 개수) - (오른쪽을 바라보는 금색 돌상의 개수) |

# 창영이는 궁극의 깨달음을 얻을 수 있을까?

n= int(input())
dolsang = list(map(int,input().split()))
# cnt = 1

# left = 0
# right = 0

# ans_l=0
# ans_r=0

start = dolsang[0]  
# for idx in range(1, len(dolsang)):

#     if start == dolsang[idx]: # 연속이면서
#         if dolsang[idx] == 1: # 왼쪽을 보고있으면
#             cnt += 1
#             left = cnt
#         elif dolsang[idx] == 2:               # 오른쪽
#             cnt += 1
#             right = cnt
#         start = dolsang[idx] # 비교대상 갱신
        
#     else: #연속이 아니라면
#         ans_l += left
#         ans_r += right
#         cnt = 1
#         left=0
#         right=0
#         start = dolsang[idx]
# if abs(ans_l-ans_r):
#     print(abs(ans_l-ans_r))
# else:
#     print(1)
L=0
R=0
ans=1
if len(dolsang) > 1: 
    for i in range(1,len(dolsang)):
        if dolsang[i-1] == dolsang[i] and dolsang[i] == 1:
            L+=1
        else:
            R+=1
    ans = abs(L-R)
    print(ans)
else: print(ans)

# 5
# 1 1 2 1 2