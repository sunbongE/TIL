# 주어진 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 결과를 출력하시오.

world = 'apple'

print(world[::-1])

#강사님 풀이

word = 'apple'
result = ''
for char in word:
    result = char + result
print(result)