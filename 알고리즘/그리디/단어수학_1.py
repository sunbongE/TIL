n=int(input())  
alpabet = []
#입력
for _ in range(n):
    alpabet.append(input())
#알파벳 딕셔너리생성
alpabet_dic=dict()
#숫자로 기록예정
nums=[]

for i in range(n): # 알파벳 뭉태기들만큼 반복
    for j in range(len(alpabet[i])): # 그 뭉태기 길이만큼 반복

        if alpabet[i][j] in alpabet_dic: # 딕셔너리에 이미 알파벳이 있다면
            alpabet_dic[alpabet[i][j]] += 10**(len(alpabet[i])-j-1) #추가
        
        else:                            # 없으면 생성
            alpabet_dic[alpabet[i][j]] = 10**(len(alpabet[i])-j-1) 

#딕셔너리의 값들을 순회하면서 nums에 추가시킬거
for val in alpabet_dic.values():
    nums.append(val)
#내림차순 정렬
nums.sort(reverse=True)

ans = 0

# 큰 수부터 cur_num을 곱하고 그 값들을 더해주면 답이 된다.
cur_num = 9 
for num in nums:
    ans += num * cur_num
    cur_num -= 1
print(ans)