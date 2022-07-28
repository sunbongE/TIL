# 오타맨 고창영
case = int(input())

for _ in range(case):
    ind, word = input().split()
    print(word.replace(ind,''))