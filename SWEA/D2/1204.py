import sys
sys.stdin = open('1204.txt', 'r')

t = int(input())

for f in range(1,t+1): # 테스트 케이스 번호
    case_num = int(input())
    num_li = list(map(int, input().split())) # list안에 int형을 띄어쓰기로 구분해 입력받음
    dic = {} #결과받을 딕셔너리 하나 만듬
    for i in num_li: #리스트 안에 값을 순회하면서 
        dic[i] = dic.get(i,0)+1 #추가 및 생성
        #딕셔너리에 넣어서 각 수마다 몇번 나오는지 계산할것
    new_dic = sorted(dic, key = lambda x:dic[x], reverse = True) # x = key,dic[x] = value 벨류를 기준으로 정렬이라는 뜻
    # value를 기준으로 내림차순 정렬
    print(f'#{f} {new_dic[0]}')

