# 문자열 word가 주어질 때, 해당 문자열에서 a 의 모든 위치(index)를 출력해주세요.
# find() index() 메서드 사용 금지\\

#input
word = 'HappyHacking'
#output = 1 6
index_a = 0
cnt = 0
for i in word:
    cnt += 1
    if i == 'a':
        index_a += cnt
        print(index_a-1, end=' ')
        index_a = 0



