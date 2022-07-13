# 주어진 문자열 word가 주어질 때, 해당 단어에서 ‘a’를 모두 제거한 결과를 출력하시오.


world = 'apple'

for i in world:
    if i == 'a' :
        continue
    
    print(i, end = '')


