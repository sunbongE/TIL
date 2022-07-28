# 카드놀이


a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_score = 0
b_score = 0
status_ = []

for i in range(10):
    if a[i] > b[i]:
        a_score += 3
        status_.append('A')
    elif a[i] < b[i]:
        b_score += 3
        status_.append('B')
    elif a[i] == b[i]:
        a_score += 1
        b_score += 1
# print(a_score, b_score)
# 점수가 같을 때
if a == b:
    print(a_score, b_score)
    print("D")    
elif a_score == b_score:

    print(a_score, b_score)
    print(status_[-1])      


else:
    print(a_score, b_score)
    if a_score > b_score:
        print('A')
    else:
        print('B')
