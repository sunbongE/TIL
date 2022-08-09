height = []
for i in range(9):
    height.append(int(input()))   # 아홉 난쟁이의 키를 리스트로 받는다

for i in height:
    for j in height:
        if sum(height) - i - j == 100 and i != j:       # 아홉 난쟁이의 키 리스트를 전부 더하고 2명의 값을 뺀 값이 100, 9명의 키는 모두 다르기에 i = j

            height.remove(i)
            height.remove(j)

height.sort()                                           # 오름차순 정렬

for i in height:
    print(i)
