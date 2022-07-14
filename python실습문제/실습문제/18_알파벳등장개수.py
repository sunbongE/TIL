# 문자열 word가 주어질 때, Dictionary를 활용해서
# 해당 문자열에서 등장한 모든 알파벳 개수를 구해서 출력하세요.
# 추가하는 법
# word_dic['b'] = 0
# print(word_dic)


d = {}
word = 'apple'
cnt = 0


for i in word:
    d[i] = 0

    for j in word:
        if i == j:
            cnt += 1

    
    d[i] += cnt
    cnt = 0
    


for k, v in d.items():
    print(k,v)


# 다른 풀이
# word = 'banana'

# d = {}

# for i in word:
#     d[i] = d.get(i, 0)+1
#     print(d)

# for key, value in d.items():
#     print(key, value)
