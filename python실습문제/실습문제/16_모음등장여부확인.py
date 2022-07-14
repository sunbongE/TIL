# 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수를 출력하시오.
# 모음 : a, e, i, o, u 
# count() 사용 금지

word = 'apple'
cnt = 0
# output 2

for i in word:
    if i == 'a':
        cnt += 1
    elif i == 'e':
        cnt += 1
    elif i == 'i':
        cnt += 1
    elif i == 'o':
        cnt += 1
    elif i == 'u':
        cnt += 1

print(cnt)

word = 'apple'
vowels = ['a', 'e', 'i', 'o', 'u']
vowels_cnt = 0
for x in word:
    for y in vowels:
        if x ==y:
            vowels_cnt += 1
print(vowels_cnt)
