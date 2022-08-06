# ## 2. 텍스트 데이터 활용 - 특정 단어 추출

# - 과일 데이터 `fruits.txt`를 활용하여 `berry`로
#  끝나는 과일의 갯수와 목록을 `02.txt`  에 기록하시오.
#     - 과일은 하나당 한 줄에 기록되어 있습니다.



with open('fruits.txt', 'r', encoding='utf-8') as f:
    test = f.read().split('\n')# 지금 리스트
#stawberry 의 길이 만큼 -> 9 
    li = []
    cnt = 0
    t = 0
    for char in test: #문자 하나씩 뽑음
        
        if char[len(char)-5:] == 'berry':
            li.append(char)
         
    li = list(set(li))
    for n in li:
        cnt+=1        
    
    
    
with open('02.txt', 'w', encoding='utf-8') as ff:
    ff.write(f'{cnt}\n')
    for word in li:
        ff.write(f'{word}\n')
