#최빈수 구하기
#최빈수 = 가장 많이 나오는애
import sys
sys.stdin = open('최빈수.txt','r')

case = int(input())

for t in range(1,case+1):
    dic_nums = dict()
    test = int(input())
    nums = list(map(int, input().split()))

    for x in nums: #입력받은 번호들의 리스트를 순회하며 
        dic_nums[x] = dic_nums.get(x,0) + 1 # 딕셔너리에 x를 key로 만들고 없으면 0으로 value 저장 있을때 1증가  

        result = sorted(dic_nums, key= lambda x:dic_nums[x],reverse=True) # sorted함수의 람다를 이용해 value를 기준으로 내림차순 정렬시킴
    print(f'#{t} {result[0]}') #형식에 맞춰 출력, result에 가장 첫번째 즉, value가 높은 넘을 출력했다.