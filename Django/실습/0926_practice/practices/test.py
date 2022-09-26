import random
a = {'q': ['10', '100']}


st = ['강아지','고양이','소','말','망아지','돼지','표범']
cnt = 3
leng = 10
result = []
for _ in range(int(cnt)):
    word=''
    for _ in range(int(leng)):
        r = random.choice(st)
        # print(r)
        word += r+' '
    result.append(word)
for f in result:

    print(f)