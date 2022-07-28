word = input().upper()

del_w = 'CAMBRIDGE'

for w in del_w:
    a = word.find(w)
    if a != -1:
        new_word = word.replace(w,'')
        word = new_word
print(word)