with open('fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()
    li = text.split('\n')
    cnt = 0
    for n in li:
        cnt += 1
    print(cnt)
    print(text)