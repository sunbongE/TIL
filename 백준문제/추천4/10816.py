import sys 
sys.stdin = open('10816.txt','r')
N = int(input())
cards = [*map(int, input().split())]
M = int(input())
candidate = [*map(int, input().split())]
# print(cards)

# 10
# 6 3 2 10 10 10 -10 -10 7 3
# 8
# 10 9 -5 2 3 4 5 -10
count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1
# print(count) #N의 값을 딕셔너리 형으로 정리함
#  {6: 1, 3: 2, 2: 1, 10: 3, -10: 2, 7: 1}

for target in candidate:
    result = count.get(target)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")
