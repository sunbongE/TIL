# 딕셔너리 사용
# 입력받은 리스트를 순회하면서 딕셔너리에 추가한다.
# value는 인덱스를 0부터 증가시켜 넣어준다.
# 가장 필요한 것은 오름차순 정렬 후 넣는것이다.

n = int(input())

li = list(map(int, input().split()))
# 정렬
sort_li = sorted(list(set(li)))

# 사전
dogam = dict()

for idx in range(len(sort_li)):
    dogam[sort_li[idx]] = idx

for num in li:
    print(dogam[num], end=" ")

# print(dogam)
