import sys
sys.stdin = open('모음의개수.txt','r')

# 'a', 'e', 'i', 'o', 'u' 이거 찾는 문제

# print(dic.get('x'))
while 1:
    dic={
    'a':0, 
    'e':0,
    'i':0,
    'o':0,
    'u':0
}
    st = input().lower()
    re = 0 
    # print(st)
    if st == '#':
        break
    else:
        for word in st:
            for w in word:
                if dic.get(w) != None:
                    dic[w]=dic.get(w)+1
    for a in dic.values():
        re += a
    print(re)
