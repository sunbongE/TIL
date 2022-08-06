# 과일 데이터 fruits.txt를 활용하여 과일의 이름과 등장 횟수를  03.txt 에 기록하시오.

with open('fruits.txt', 'r', encoding='utf-8') as f:
    list_f = f.read().split()
    new = {}
    
    
    for word in list_f:
        new[word] = new.get(word,0) + 1
    
    
    
with open('03.txt', 'w', encoding='utf-8') as ff:
    for key in new:

        ff.write(f'{key} {new[key]}\n')

